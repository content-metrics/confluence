#!/bin/bash 

# PostgreSQL Docker Image in iterative mode (bash)

image_name=media-postgres
echo "Enter the postgres password!"
read postgrespassword

docker pull postgres:alpine
docker cp . /home 
docker run --name $image_name -e POSTGRES_PASSWORD=$postgrespassword -d -p 5432:5432 postgres:alpine
docker exec -it $image_name bash

# To quit the interactive mode use command ctrl D 