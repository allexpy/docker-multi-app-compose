```
Build an image:

-t is the tag (name of the image)
-f the actual Dockerfile building
. the current directory

docker build -t my-nginx -f Dockerfile.nginx .
```

```
Running a container image:
my-nginx is the image tag
-p 8080:80 port mapping

docker run -p 8080:80 my-nginx
```

```
Get inside container:
-it interactive mode
docker run -it my-nginx /bin/bash
```


```
docker ps
```