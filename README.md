# CarsSeles
*this is my CarsSeles Project

Config Database Docker: 

docker run -p 127.0.0.1:3306:3306  --name mdb -e MARIADB_ROOT_PASSWORD=Password123! -d mariadb:latest

docker exec -it mdb mariadb --user root -pPassword123!
