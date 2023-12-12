Write-Host "Running followerbot container"
Write-Host "------------------------------------------------------------------------"

# Run docker command, mounting directory for output and using unbuffered output
docker run -v "${PWD}\..\..\:/code/" -it followerbot python -u /code/src/bot.py

Write-Host "------------------------------------------------------------------------"
