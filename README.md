
docker-compose up
docker exec -it $(docker-compose ps -q db ) psql -Upostgres -c 'create database flaskbyexample;'



docker exec -it $(docker-compose ps -q db ) psql -Upostgres -c '\z'

create database flask-by-example
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

heroku addons:create heroku-postgresql:hobby-dev --app felipear89-flask1
heroku config --app felipear89-flask1
heroku run python manage.py db upgrade --app felipear89-flask1

docker-compose build