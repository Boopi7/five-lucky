import subprocess, requests, json

from datetime import (
    datetime, timezone, timedelta)
from django.conf import settings

from lottery.models import (Lottery,
    Bet)
from lottery.cardano.operations import (
    generate_minting_policy)


# Every Monday 00:00 UTC
def new_lottery():
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

    # Create lottery object
    lottery = Lottery.objects.create(
        policy_id=policyID,
        draw_date=draw_date)


# Every Sunday 09:00 UTC
def draw_luckyfive():
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

    while (status_code != 200):
        response = requests.post(
            'https://api.random.org/json-rpc/4/invoke',
            data=json.dumps(payload),
            headers=headers)
        status_code = response.status_code

        if status_code == 200:
            response_dict = response.json()

            if 'error' in response_dict.keys():
                status_code = 500
                print('Error processing request. Retrying.')
            else:
                print('Request Successful!')

                # Get current lottery
                current_lottery = Lottery.get_current_lottery()
                current_lottery.lucky_five = response_dict
                current_lottery.save()

                # Draw lottery winners
                lucky_five = response_dict.get(
                    'result').get('random').get('data')[0]
                print(lucky_five)

                winners = Bet.objects.filter(
                    lottery=current_lottery,
                    lucky_five=lucky_five,
                    is_active=True)
                print(winners)

                # Deactivate current lottery
        else:
            print('Error processing request. Retrying.')

    pass
