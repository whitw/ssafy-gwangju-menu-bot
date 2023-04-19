#!/bin/sh
sudo apt install docker.io
sudo docker rm -f $(sudo docker ps --filter ancestor=gwangju-menubot -q)
sudo docker rmi gwangju-menubot
sudo docker build -t gwangju-menubot .
sudo docker run -d gwangju-menubot
