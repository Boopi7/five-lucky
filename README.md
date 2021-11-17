# lucky-five
A simple betting game on cardano blockchain

## Setup

1. Download `cardano-cli` and add it to your path.

2. Create the policy directory that will be used to store
policy related files for minting ticket-nfts.

	`mkdir -p /home/user/luckyfive/policy`

3. Create the payment directory to store payment key-pair
used for the betting module.

	`mkdir -p /home/user/luckyfive/payments`

4. Create a local database for the site

5. Create a config file (e.g /etc/config.json)

	```
	{
		"DEBUG": true,
		"SECRET_KEY": "xxxx",
		"ALLOWED_HOSTS": [],
		"DB_NAME": "luckyfive",
		"DB_USER": "luckyfive_user",
		"DB_PASSWORD": "luckyfive_password",
		"DB_HOST": "localhost",
		"POLICY_DIR": "",
		"PAYMENT_SKEY": "",
		"PAYMENT_VKEY": ""
	}
	```