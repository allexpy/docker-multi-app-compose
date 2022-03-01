```
Build an image:

-t is the tag (name of the image)
-f the actual Dockerfile building
. the current directory

docker build -t php-app -f Dockerfile.php-app .
```

```
Running a container image:
express-app is the image tag
-p 8080:80 port mapping

docker run -p 8083:8000 -e PORT=8000 php-app
```

```
Get inside container:
-it interactive mode
--rm removes the image at the end
docker run -it --rm php-app /bin/bash
```


```
docker ps
```