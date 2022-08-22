# confluence
intelligence marketing for influencers

## Process for create a table 
- run in your terminal inside database directory (create the docker image)
* image_name = content-metrics
$docker build -t content-metrics .  
- create docker image for postgres 
* container_name = media-database
$docker run --name media-database -d content-metrics 
- launch the image with bash 
$docker exec -it media-database bash
- inside the container env 
$source create_table.sh
- To see the table 
bash$ \dt 

![](image.png)