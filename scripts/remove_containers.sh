#!/bin/bash

# Stop and remove the containers
echo "Attempting to stop: docker-standalone-chrome"
sudo docker stop docker-standalone-chrome

echo "Attempting to remove: docker-standalone-chrome"
sudo docker remove docker-standalone-chrome


echo "Attempting to stop: followerbot"
sudo docker stop followerbot

echo "Attempting to remove: followerbot"
sudo docker remove followerbot