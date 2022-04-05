```
Build an image:

-t is the tag (name of the image)
-f the actual Dockerfile building
. the current directory

docker build -t django-app-1 -f Dockerfile.django-app .
```

```
Running a container image:
py-app-1 is the image tag
-p 8085:80 port mapping

docker run -p 8085:8000 django-app-1
```

```
Get inside container:
-it interactive mode
--rm removes the image at the end
docker run -it --rm py-app-1 /bin/bash
```


```
docker ps
```