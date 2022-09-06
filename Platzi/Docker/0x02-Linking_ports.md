### Create a container with Nginx
* sudo docker run -d --name proxy nginx
Upon looking in the process we realize this is runinning in the container's port 80

### Link the local machine port 8080 to the container's port 80
* sudo docker run -d -p 8080:80 -name proxy nginx

### Ckeing Nginx logs
* sudo docker logs proxy

### Other commands
* sudo docker exec -it containername bash (to open the terminal of an active container)
