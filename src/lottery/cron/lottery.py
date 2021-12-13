import subprocess, requests, json

from datetime import (
    datetime, timezone, timedelta)
from django.conf import settings

from lottery.models import (Lottery,
    Bet, LotteryWinner)
from lottery.cardano.operations import (
    generate_minting_policy)


# Every Monday 00:00 UTC
def new_lottery():
    try:
        if Lottery.get_current_lottery():
            raise Exception(
                'There\'s still an ongoing lottery')

        # Create directory for the new policy
        today = datetime.now(timezone.utc)
        policy_path = settings.POLICY_DIR + \
            today.strftime('%m_%d_%y')
        subprocess.run(['mkdir', '-p', policy_path])

        # Generate minting policy for the
        # ticket nfts of this lottery
        policyID = generate_minting_policy(policy_path)

        # Get lottery draw date
        offset = 6 - today.weekday()
        lottery_day = today + timedelta(days=offset)
        draw_date = datetime(
            lottery_day.year, lottery_day.month,
            lottery_day.day,
            hour=9, minute=0,
            second=0, microsecond=0,
            tzinfo=timezone.utc
        )

        # Get lotter sequence
        seq = 1
        latest_lottery = Lottery.objects.last()
        if latest_lottery:
            seq = latest_lottery.seq + 1

        # Create lottery object
        lottery = Lottery.objects.create(
            policy_id=policyID,
            draw_date=draw_date,
            seq=seq)
    except Exception as e:
        print(e)


# Every Sunday 09:00 UTC
def draw_winners():
    # Generate luckyfive number
    status_code = 0
    headers = {'Content-Type': 'application/json'}
    payload = {
        'jsonrpc': '2.0',
        'method': 'generateSignedIntegerSequences',
        'params': {
            'apiKey': settings.LUCKYFIVE_API_KEY,
            'n': 1,
            'length': 5,
            'min': 0,
            'max': 9,
            'base': 10,
            'userData': 'LuckyFive Weekly Draw'
        },
        'id': 1
    }

    try:
        # Get current lottery
        current_lottery = Lottery.get_current_lottery()
        if current_lottery is None:
            raise Exception('No active lottery')
        print('Drawing Luckyfive for: {}'.format(
            current_lottery))

        response = requests.post(
            'https://api.random.org/json-rpc/4/invoke',
            data=json.dumps(payload),
            headers=headers)
        status_code = response.status_code
        response_dict = response.json()

        if 'error' in response_dict.keys():
            error_obj = response_dict.get('error')
            status_code = error_obj.get('code')
            message = error_obj.get('message')
            raise Exception(message)
        elif status_code == 200:
            print('Request Successful!')

            # Draw lottery winners
            lucky_five = response_dict.get(
                'result').get('random').get('data')[0]
            print('Luckyfive is: {}'.format(lucky_five))

            winning_bets = current_lottery.active_bets.filter(
                lucky_five=lucky_five)
            lottery_winners = list(LotteryWinner(
                bet=bet, lottery=current_lottery)
                for bet in winning_bets)
            LotteryWinner.objects.bulk_create(
                lottery_winners)
            print('Lottery Winners: {}'.format(lottery_winners))

            # Deactivate current lottery
            current_lottery.api_response = response_dict
            current_lottery.is_active = False
            current_lottery.save()
        else:
            raise Exception('Unable to process request. Retrying.')
    except Exception as e:
        print(e)
