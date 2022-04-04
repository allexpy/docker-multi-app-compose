```
docker image prune -a  - deletes unused images
docker container prune  - deletes all stopped containers

docker compose up  - starts container
docker compose down  - stops container

docker compose build --no-cache  - rebuild from scratch


ENDPOINTS:

python: http://localhost:8080/python/
python: http://localhost:8080/python/extended/
php: http://localhost:8080/php/
php: http://localhost:8080/php/extended/  ???
javascript: http://localhost:8080/javascript/
javascript: http://localhost:8080/javascript/extended/
go: http://localhost:8080/go/
go: http://localhost:8080/go/extended/
staticfiles: http://localhost:8080/static/
```

```
Automated volume creation:

docker run -v myvolume:/where/to/mount container-image
```

```
Manual volume creation:

docker run -v /abs/path/to/localdata:/where/to/mount/ 
```

```
### Database:

docker pull postgres

docker run -p 6543:5432 -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mytestpw -d postgres

docker run -it --rm postgres /bin/bash
# psql -U myuser
```