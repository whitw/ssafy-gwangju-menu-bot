#!/bin/sh
sudo apt install docker.io
sudo docker build -t gwangju-menubot .
sudo docker run -d gwangju-menubot
