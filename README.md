
docker-compose up

docker exec -it $(docker-compose ps -q postgres9 ) psql -Upostgres -c '\z'

create database flask-by-example