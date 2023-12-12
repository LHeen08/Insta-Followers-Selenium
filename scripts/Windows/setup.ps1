# This script should run the selenium container and build the follower bot
docker run -d -p 4444:4444 -v /dev/shm:/dev/shm --name docker-standalone-chrome selenium/standalone-chrome

# Build the bot container
docker build -t followerbot ../../