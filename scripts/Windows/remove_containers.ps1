# Stop and remove the containers
Write-Host "Attempting to stop: docker-standalone-chrome"
docker stop docker-standalone-chrome

Write-Host "Attempting to remove: docker-standalone-chrome"
docker rm docker-standalone-chrome

Write-Host "Attempting to stop: followerbot"
docker stop followerbot

Write-Host "Attempting to remove: followerbot"
docker rm followerbot
