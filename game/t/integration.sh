#! /usr/bin/bash

server_running=$(curl -s localhost:8899/webserver_check.html);

if [ "$server_running" = "test" ]; 
then
  echo "Server is running";
else
  echo $server_running ;
  echo "Server is not running";
fi
