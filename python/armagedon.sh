removecontainers() {
    docker stop $(docker ps -aq)
    docker rm $(docker ps -aq)
}


removecontainers
docker network prune -f
docker rmi -f $(docker images --filter dangling=true -qa)
docker volume rm $(docker volume ls --filter dangling=true -q)
#docker rmi -f $(docker images -qa)
