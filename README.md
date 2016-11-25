## Requirements
You can run the project using docker-compose or local.
If you want to run local then you will need:
- autoenv
- postgres

## Run without docker
- Create a virtualenv
`virtualenv venv`
- Activate virtualenv
`source venv/bin/activate`
- Install dependencies:
`pip install -r requirements.txt`
- Create a database on PostgreSql
```
psql postgres
create database flaskbyexample
```
- Run `python manage.py migrate` and `python manage.py runserver`


## Run with docker
- Build and run docker-compose
`docker-compose build && docker-compose up`
- Create database inside docker
`docker exec -it $(docker-compose ps -q db ) psql -Upostgres -c 'create database flaskbyexample;'`
- Stop docker-compose and run `docker-compose up`

## Manage migrations
Read about [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## Heroku
There are files used to deploy this project to heroku
- Procfile
- runtime.txt

You need to add `heroku addons:create heroku-postgresql:hobby-dev --app {app_name}`

To see the app configs: `heroku config --app felipear89-flask1`
To run db upgrade `heroku run python manage.py db upgrade --app felipear89-flask1`