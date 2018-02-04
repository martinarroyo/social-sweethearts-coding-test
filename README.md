# Social Sweethearts Coding Test

A simple Django app with Facebook Login integration.

## Development setup:

* Edit the `deployment/fixtures.json` and fill the missing private keys.
* Run the following commands from the root directory. The default database is SQLite, so there is no need for database setup.

```bash
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata deployment/fixtures.json
```

Note that the [deauthorize callback](https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow/v2.1#deauth-callback) is only available over HTTPS, and your machine needs to be reachable outside your network. You can set up something like [this](https://stackoverflow.com/a/8025645).


## Production setup

A simple configuration for a production setup is included in the `deployment` directory.
* Again edit the `deployment/fixtures.json` file. Create the `envvars.sh` and `my.cnf` files from their `.sample` counterparts, and fill the missing values.
* Run `bash deployment/build.sh`
* Link the `social_sweethearts_coding_test.nginxconf` file to your nginx server and the `social_sweethearts_supervisord` to your instance of [`supervisor`](http://supervisord.org/)
