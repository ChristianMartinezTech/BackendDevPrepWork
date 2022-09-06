# Data in Docker

### To Bind Mount (Save locally the info of a repo)
* sudo docker run -d --name db -v localpath:containerpath
This also works to mount a container with existing information :)

### Volumes (A more secure/standard way to save and load data from/to containers)
* sudo docker volume create volumename
* sudo docker run -d --name db --mount src=volume,dst=destination containerimage
* docker volume ls
* docker volume inspect volumename
* docker volume rm volumename

* Recommended read: https://docs.docker.com/storage/volumes/

### Insert and extract files from containers
* docker cp file containername:/path/file (to copy from the machine to the container)
* The oposite order after file, to copy from the container to the local machine


### Other commands
* sudo docker exec --it {containername} bash (to open the terminal of an active container)

sudo docker stop mongo ubuntu nginx hello-world && sudo docker rm mongo ubuntu nginx hello-world