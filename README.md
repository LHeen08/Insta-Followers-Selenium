<h1 align="center">
Instagram Followers Checker bot :robot:
</h1>

Instagram bot, using selenium, that checks users who don't follow you back, and users who you don't follow back.

|<p align="center"> :warning: WARNING          </p>|
|:---------------------------|
|1. This is not recommended to be used when you have A LOT of followers. It is very slow as followers increase because of selenium scraping all followers.|
|2. This will not work with two factor authentication enabled, it must be disabled to allow sign in.|
|3. I advise to not use this repeatedly, as too many sign in attempts will not allow you to sign in and will be shown a "Please wait a few minutes before you try to login again"|
<br />

##### :exclamation::exclamation::exclamation:I am not responsible for any damages. Use at your own risk. Look through the code if you feel uneasy or don't use it...
<br />


# Requirements
- Please follow the appropriate instructions on how to install docker on your machine: 
  - [Docker setup](https://docs.docker.com/get-docker/)
  
# Installation
Clone this repository to a local directory on your machine:
```
git clone git@github.com:LHeen08/Insta-Followers-Selenium.git
```
Move into that directory.
<br />

## Usage
There is a scripts folder to allow simple usage of running and creating the containers.
<br />
You can use the .sh scripts for Linux/MacOS or use the Windows/.ps1 scripts for running on Windows.

The process is the same for each OS, just the names will be different
1. Run the setup.sh (Linux/MacOS) or the setup.ps1 (Windows) to setup the docker containers
    - Linux/MacOS
    ```
    ./setup.sh
    ```
    - Windows
    ```
    setup.ps1
    ```
3. Once the docker-standalone-chrome container is running, navigate to [localhost:4444](http://localhost:4444) and copy the "URI" that is listed on the selenium grid box
4. With that copied URI, go to the cloned directory and open the "input_file.py" and paste it into the "connection_url".
   - It should now look similar to this:
     ```
     connection_url = "http://172.17.0.2:4444"
     ```
5. While still inside input_file.py: 
    - Enter your username and password for Instagram
    ```
    username = "username"
    password = "password"
    ```
6. Save the file
7. Run the followerbot container with the "*run*" script
    - Linux/MacOS
    ```
    ./run.sh
    ```
    - Windows
    ```
    run.ps1
    ```
8. Let the container run and you should see a file appear called: not_following.txt
  - If you open that file you should be able to see all users that dont follow you and all users that you dont follow
9. To remove the containers, run the "*remove_containers*" script
    - Linux/MacOS
    ```
    ./remove_containers.sh
    ```
    - Windows
    ```
    remove_containers.ps1
    ```
