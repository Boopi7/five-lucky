# lucky-five
A simple betting game on cardano blockchain

## Development

1. [Set up a local cardano node.](https://developers.cardano.org/docs/get-started/installing-cardano-node)

2. [Install PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart) and create a dedicated user and database for development.

3. Create the policy directory that will be used to store
policy related files for minting ticket-nfts.

	`mkdir -p $HOME/.luckyfive/policy`

4. Create the payment directory to store payment key-pair
used for the betting module.

	`mkdir -p $HOME/.luckyfive/payment`

5. Clone the repository.

	`git clone https://github.com/riidatibula/lucky-five.git`

6. Create a json config file.

	`sudo touch /etc/luckyfive-config.json; sudo -e /etc/luckyfive-config.json`

	Enter the your actual development configuration:

	```
	{
        "DEBUG": true,
        "SECRET_KEY": "xxxxxxxx-secret-key-xxxxxxxx",
        "LUCKYFIVE_API_KEY": "xxxxxxxx-api-xxxxxxxx",
        "ALLOWED_HOSTS": [],
        "DB_NAME": "luckyfive",
        "DB_USER": "luckyfivedb",
        "DB_PASSWORD": "mystrongpassword",
        "DB_HOST": "localhost",
        "POLICY_DIR": "$HOME/.luckyfive/policy/",
        "PAYMENT_SKEY": "$HOME/.luckyfive/payment/payment.skey",
        "PAYMENT_VKEY": "$HOME/.luckyfive/payment/payment.vkey"
	}
	```

7. Create a virtual environment under the cloned project.

	`cd <project-directory>; python3 -m virtualenv .venv` 

8. Activate virtualenv.

	`source .venv/bin/active`

9. Install dependencies.

	`pip -r install requirements.txt`

10. Run project. The default local development url is at [localhost:8000](http://localhost:8000).

	`python src/manage.py runserver`