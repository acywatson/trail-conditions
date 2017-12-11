trail-conditions

## How to start the virtual environment
1) run source ~/Python/python-virtual-environments/env/bin/activate
2) spin up the server by running python3 ~/Python/CornerCanyon/manage.py runserver
2.5) if an error occurs during the server spin-up, check here: https://coderwall.com/p/rwgkzw/wtf-is-the-server-running-locally-and-accepting-connections-on-unix-domain-socket-tmp-s-pgsql-5432
3) open browser to http://localhost:8000

## How to perform database migrations
python3 manage.py migrate

## How to run unit tests
python3 manage.py test
