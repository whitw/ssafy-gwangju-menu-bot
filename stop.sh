#!/bin/sh
sudo docker rm -f $(sudo docker ps -f ancestor=gwangju-menubot -q)
sudo docker rmi gwangju-menubot
