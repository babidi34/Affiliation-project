#!/bin/bash

conteneur_name="pelican-test"
image_name="debian-pelican-plus"

docker rm -f  $conteneur_name

docker build -t $image_name .

docker run --env-file=.env -tid --name $conteneur_name $image_name

docker exec $conteneur_name hostname -I
sleep 1
docker logs $conteneur_name