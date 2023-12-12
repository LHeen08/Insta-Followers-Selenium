#!/bin/bash

echo "Running followerbot container"
echo "------------------------------------------------------------------------"

# Run docker command, mounting directory for output and using unbuffered output
sudo docker run -v $PWD/../:/code/ -it followerbot python -u /code/src/bot.py

echo "------------------------------------------------------------------------"
