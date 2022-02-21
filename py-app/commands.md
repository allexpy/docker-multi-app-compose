```
Build an image:

-t is the tag (name of the image)
-f the actual Dockerfile building
. the current directory

docker build -t py-app-1 -f Dockerfile.py-app .
```

```
Running a container image:
py-app-1 is the image tag
-p 8080:80 port mapping

docker run -p 8080:8000 py-app-1
```

```
Get inside container:
-it interactive mode
docker run -it py-app-1 /bin/bash
```


```
docker ps
```