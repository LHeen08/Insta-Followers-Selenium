<h1 align="center">
Instagram Followers Checker bot :robot:
</h1>

Instagram bot, using selenium, that checks users who don't follow you back, and users who you don't follow back.

|<p align="center"> :warning: WARNING          </p>|
|:---------------------------|
|1. This is not recommended to be used when you have A LOT of followers. It is very slow as followers increase because of selenium. This was created to practice using selenium.|
|2. This will not work with two factor authentication enabled, it must be disabled to allow sign in.|
<br />

##### :exclamation::exclamation::exclamation:I am not responsible for any damages. Use at your own risk. Look through the code if you feel uneasy or don't use it...
<br />

***The terminal commands provided are for unix/linux. If on Windows they will differ but will be somewhat similar, refer to correct documentation accordingly.***
<br />

# Requirements
- Please follow the appropriate instructions on how to install docker on your machine: 
  - [Docker setup](https://docs.docker.com/get-docker/)
  
## Optional
- If you wish to view the output lists on a easier to read text file (compared to seeing the list on the terminal), then you will need Python 3.8 and pip3 on your local machine
  - How to [Install](https://realpython.com/installing-python/) and [Run](https://realpython.com/run-python-scripts/) Python
  - How to [Install](https://pip.pypa.io/en/stable/installing/) pip3
  
# Installation
Clone this repository to a local directory on your machine:
```
git clone https://github.com/LHeen08/Insta-Followers-Selenium.git
```
Then cd into that directory that you just cloned
<br />

#### Start the docker selenium container
Run this command to start the selenium web driver container:
```
docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-firefox:4.0.0-beta-1-prerelease-20210207
```
Check to make sure the container is running:
```
docker ps
```
<br />

Once the selenium docker container is up and running, navigate to [localhost:4444](http://localhost:4444) on your browser
- Copy the *URI:* IP address
- Open the *Input_file.py* from this project. (With any text editor)
  - Paste the *URI*: IP address that you had previously copied in the *connection_url* variable (without the brackets { } )
    
```
connection_url = "{PASTE IT HERE}"
```
  
- While inside the Input_file.py file: 
    - Enter your username and password for Instagram (without the brackets { } )
      
```
username = "{ENTER USERNAME HERE}"
password = "{ENTER PASSWORD HERE}"
```
- Save Input_file.py

# Usage
### a. Docker
Build and run the container using docker:
  - *Make sure you are in the directory that holds the files...the one cloned from earlier!*
```
docker build -t followerbot .
```
```
docker run followerbot
```
Let it run, if you have quite a few followers and following it may take a while (refer to warning at top of README)

### b. Python on local machine
Again if you wish to have a neater output to a file, you need Python on your local machine (refer to Optional section in README)
<br />

It is necessary to change the connection url when running python on the local machine
  - Change the connection_url to http://localhost:4444
```
connection_url = "http://localhost:4444"
```

<br />

Install the requirements for the project
```
pip3 install -r ./requirements.txt
```
<br />

Run the python file
```
python3 bot.py
```
After successfully running this command, check the output.txt file for a neat readable output

<br />

#### To stop docker containers:
See running containers
```
docker ps
```

Stop unwanted containers (replace {Container ID} with the correct ID of container found with docker ps)
```
docker stop {CONTAINER ID}
```
  - [Help](https://docs.docker.com/engine/reference/commandline/stop/) stopping docker containers
