import time
import traceback
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from input_file import username, password, connection_url
from selenium.webdriver.chrome.options import Options


# Log in to instagram
def login(driver):
    driver.get("https://www.instagram.com/accounts/login") # Go to instagram login page
    time.sleep(2)
    assert "Instagram" in driver.title

    # Is there a popup we need to go around?

    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Logging in: {username}")

    # Get the elements to enter 
    username_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    # Now clear the inputs and send keys
    username_input.clear()
    username_input.send_keys(username)

    password_input.clear()
    password_input.send_keys(password)    

    login_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_btn.click()
    time.sleep(5) # wait a bit for the page to load to login



# Function to get the followers
def get_followers(driver):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Getting followers...")

    driver.get(f'https://www.instagram.com/{username}/') # navigate to the user page and get the followers
    time.sleep(2)
    
    # Get the number of followers ### NOTE: this might have to change, not sure if the class will always be called this
    followers_element = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located ((By.XPATH, "(//span[@class='_ac2a'])[2]"))
    )    
    followers_number = int(followers_element.get_attribute("title"))
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Total followers: ", followers_number)  # Output followers number
    
    
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located ((By.XPATH, "//a[contains(@href, '/followers')]"))).click()
    time.sleep(2)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Getting all followers for {username}")

    users = set() # set to hold followers

    # Find following elemnent 
    followers_list_elem = WebDriverWait(driver, 15).until((EC.visibility_of_element_located ((By.XPATH, "(//div[contains(@class, '_aano')])"))))
    # Now get the child element (so not the suggested users)
    child_followers_list = followers_list_elem.find_element(By.XPATH, ".//div[contains(@style, 'display')][1]")

    while len(users) < followers_number:
        # keep getting the list of following as we scroll through and update the list updates as we scroll
        followers = child_followers_list.find_elements(By.XPATH, ".//a[contains(@href, '/')]")

        # With all the followers, see if they exist in the set 
        for i in followers:
            if i.get_attribute('href'):
                users.add(i.get_attribute('href').split("/")[3]) # add user to the set 
            else:
                continue
            
        # Update the progress bar based on the current set size
        progress = min(len(users) / followers_number * 100, 100)  # Calculate progress percentage
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Progress: [{int(progress):3}%] [{'[' + '=' * int(progress) + ' ' * (100 - int(progress)) + ']':100}]")

        ActionChains(driver).send_keys(Keys.END).perform()
        time.sleep(1)

    users = list(users)  # Trim the user list to match the desired number of followers
    print("\n")
    return users # return the list 


# Function to get the following
def get_following(driver):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Getting following...")

    driver.get(f'https://www.instagram.com/{username}/') # navigate to the user page and get the following
    time.sleep(2)
    
    # Get the number of following ### NOTE: this might have to change, not sure if the class will always be called this
    following_element = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located ((By.XPATH, "(//span[@class='_ac2a'])[3]"))
    )
    child_span_elem = following_element.find_element(By.XPATH, ".//span[contains(@class, 'html-span')]")
    following_number = int(child_span_elem.text)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Total following: ", following_number)  # Output following number
    
    
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located ((By.XPATH, "//a[contains(@href, '/following')]"))).click()
    time.sleep(2)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Getting all following for {username}")

    users = set() # set to hold followers


    # Find following elemnent 
    following_list_elem = WebDriverWait(driver, 15).until((EC.visibility_of_element_located ((By.XPATH, "(//div[contains(@class, '_aano')])"))))
    # Now get the child element (so not the suggested users)
    child_following_list = following_list_elem.find_element(By.XPATH, ".//div[contains(@style, 'display')][1]")

    while len(users) < following_number:
        # keep getting the list of following as we scroll through and update the list updates as we scroll
        following = child_following_list.find_elements(By.XPATH, ".//a[contains(@href, '/')]")

        # With all the followers, see if they exist in the set 
        for i in following:
            if i.get_attribute('href'):
                users.add(i.get_attribute('href').split("/")[3]) # add user to the set (just the username from the href)
            else:
                continue
            
        # Update the progress bar based on the current set size
        progress = min(len(users) / following_number * 100, 100)  # Calculate progress percentage
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Progress: [{int(progress):3}%] [{'[' + '=' * int(progress) + ' ' * (100 - int(progress)) + ']':100}]")
        ActionChains(driver).send_keys(Keys.END).perform()
        time.sleep(1)

    print("\n")

    users = list(users)  # Trim the user list to match the desired number of following

    return users # return the list




# Main driver 
if __name__ == '__main__':
    try:
        if connection_url == "":
            print("Empty connection_url. Please enter a connection URL in input_file.py")
            exit(1)

        if username == "" or password == "":
            if username == "":
                print("Caution, empty username. If this is incorrect, add a username in input_file.py")
            if password == "":
                print("Caution, empty password. If this is incorrect, add a password in input_file.py")


        # Init driver to use
        options = Options()
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-gpu")
        options.add_argument("--log-level=3")
        mobile_emulation = {
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Remote(connection_url, options=options)


        login(driver)
        followers = get_followers(driver)
        following = get_following(driver)
        
        # Finding users in followers list but not in following list
        not_following = [user for user in followers if user not in following]

        # Finding users in following list but not in followers list
        not_following_you = [user for user in following if user not in followers]

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Saving results to: not_following.txt")

        # Write the lists to the file within the src directory
        with open("not_following.txt", 'w') as file:
            file.write(f"Users not following you back: Count - {len(not_following_you)}\n")
            file.write("------------------------------------------------------------\n")
            file.write("\n".join(not_following_you))
            file.write("\n------------------------------------------------------------")
            file.write(f"\n\n\nUsers you are not following back: Count - {len(not_following)}\n")
            file.write("------------------------------------------------------------\n")
            file.write("\n".join(not_following))
            file.write("\n------------------------------------------------------------\n")


    except Exception as e:
        # Handle exceptions here, you can print the error or perform specific actions
        print(f"An error occurred: {e}")
        traceback.print_exc()

    finally:
        # Ensure the WebDriver is safely terminated regardless of exceptions
        if 'driver' in locals():
            driver.quit()  # Quit the driver session




