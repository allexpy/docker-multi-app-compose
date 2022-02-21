```
Build an image:

-t is the tag (name of the image)
-f the actual Dockerfile building
. the current directory

docker build -t express-app -f Dockerfile.nginx .
```

```
Running a container image:
express-app is the image tag
-p 8080:80 port mapping

docker run -p 8080:8000 -e PORT=8000 express-app
```

```
Get inside container:
-it interactive mode
--rm removes the image at the end
docker run -it --rm express-app /bin/bash
```


```
docker ps
```