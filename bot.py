import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities, ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from input_file import username, password, connection_url


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
mobile_emulation = {
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)



# Log in to instagram
def login(driver):
    driver.get("https://www.instagram.com/accounts/login") # Go to instagram login page
    time.sleep(2)
    assert "Instagram" in driver.title

    # Is there a popup we need to go around?

    print("Logging in...")

    # Get the elements to enter 
    username_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    # Now clear the inputs and send keys
    username_input.clear()
    username_input.send_keys(username)

    password_input.clear()
    password_input.send_keys(password)    

    login_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_btn.click()
    time.sleep(5) # wait a bit for the page to load to login


def get_followers(driver):
    driver.get(f'https://www.instagram.com/{username}/') # navigate to the user page and get the followers
    time.sleep(2)

    # Retrieve the total number of followers
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='_ac2a _ac2b']")))
    followers_number = element.text
    print("total followers: ", followers_number)  # print number of followers to screen

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/followers')]"))).click()
    time.sleep(2)
    print(f"Getting all followers for {username}")

    users = set() # set to hold followers

    while len(users) < 20:
        followers = driver.find_elements(By.XPATH, "//a[contains(@href, '/')]")

        for i in followers:
            if i.get_attribute('href'):
                users.add(i.get_attribute('href').split("/")[3])
            else:
                continue

        ActionChains(driver).send_keys(Keys.END).perform()
        time.sleep(1)

    users = list(users)[:20]  # Trim the user list to match the desired number of followers

    print(f"[Info] - Saving followers for {username}...")
    with open(f'{username}_followers.txt', 'a') as file:
        file.write('\n'.join(users) + "\n")



# Main driver 
if __name__ == '__main__':
    login(driver)
    get_followers(driver)




# #   Function to try for element returning exception if not found
# #   Parameters are a string, and type of element (xpath or css)
# def try_for_element(string, elem_type):
#     if elem_type == 'xpath':
#         try:
#             elem = WebDriverWait(driver, 5).until(
#                 EC.presence_of_element_located(
#                     (By.XPATH, string))
#             )
#             return elem
#         except NoSuchElementException:
#             print("Exception occurred, no such element (Xpath)")
#     elif elem_type == 'css':
#         try:
#             elem = WebDriverWait(driver, 5).until(
#                 EC.presence_of_element_located(
#                     (By.CSS_SELECTOR, string))
#             )
#             return elem
#         except NoSuchElementException:
#             print("Exception occurred, no such element (CSS-Selector)")
#     else:
#         print("Exception occurred no such element type" + elem_type)


# time.sleep(1)

# # get the username element to enter username
# username_element = try_for_element("//*[@id='loginForm']/div/div[1]/div/label/input", xpath)

# # get the password element to enter password
# password_element = try_for_element("//*[@id='loginForm']/div/div[2]/div/label/input", xpath)

# # send keys to enter the username and password
# username_element.send_keys(username)
# password_element.send_keys(password)

# # log in
# login_button = try_for_element("//*[@id='loginForm']/div/div[3]/button/div", xpath)
# login_button.click()


# # Sometimes a "Turn on Notifications" modal pops up, if it does click out of it
# def check_for_notif_modal():
#     try:
#         notif_modal_dismiss = driver.find_element_by_css_selector(
#             "body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
#         notif_modal_dismiss.click()
#     except:
#         return


# time.sleep(5)

# check_for_notif_modal()

# account_button = try_for_element("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span", xpath)
# account_button.click()

# profile_button = try_for_element(
#     "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div", xpath)
# profile_button.click()


# # Function to get the lists of followers
# def get_followers():
#     # DEBUG --> Timer to see performance
#     start_time = time.time()

#     # Retrieve the total number of followers
#     followers_number = try_for_element(
#         '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span', xpath)  # get number of followers
#     print("total followers: ", followers_number.text)  # print number of followers to screen

#     # Click the followers button
#     followers_button = try_for_element("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a", xpath)
#     followers_button.click()

#     # Empty list of followers
#     followers = []

#     # Modal window of followers
#     followers_panel = try_for_element('div[role=\'dialog\'] ul', css)

#     # List of followers loaded from the modal. This will start as 12 elements loaded at the start unless followers is
#     # < 12
#     loaded_followers = followers_panel.find_elements_by_css_selector('li')
#     # The followers loaded until now from the list, will update continuously
#     loaded_followers_till_now = len(loaded_followers)

#     # Action chains
#     actions = ActionChains(driver)
#     actions.move_to_element(followers_panel)
#     actions.click()
#     actions.perform()
#     actions.reset_actions()

#     index = 1

#     # followers_list = try_for_element("/html/body/div[5]/div/div/div[2]/ul", xpath)
#     items = followers_panel.find_elements_by_css_selector("ul span a")

#     #   Append the first 12 (or less) usernames to the followers list
#     for elem in items:
#         account_name = elem.text
#         followers.append(account_name)
#         index += 1

#     # Message to user
#     print("Retrieving followers list...\n")

#     # While loaded_till_now amount is less than the number of total followers, scroll and load more, populating
#     # loaded_following list
#     # Between each scroll append the usernames of the current elements to the followers list.
#     # Building the list and iterating through 12 at a time
#     while loaded_followers_till_now < int(followers_number.text):
#         # Scroll modal window
#         actions.send_keys(Keys.END)
#         actions.perform()

#         loaded_followers = followers_panel.find_elements_by_css_selector("ul span a")
#         loaded_followers_till_now = len(loaded_followers)

#         #   Append the next 12 (or less) usernames to the followers list
#         for elem in loaded_followers[index:loaded_followers_till_now]:
#             account_name = elem.text
#             followers.append(account_name)
#             index += 1

#         actions.move_to_element(followers_panel)

#     exit_button = try_for_element(
#         "body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > button", css)
#     exit_button.click()
#     print(followers, len(followers))

#     # Timer
#     print("\nTime of first loop... %s seconds\n" % (time.time() - start_time))

#     return followers


# # Function to get the lists of following
# def get_following():
#     #   Timer to see performance
#     start_time = time.time()

#     # Retrieve the total number of following
#     following_number = try_for_element(
#         '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span', xpath)
#     print("total following: ", following_number.text)  # print number of following to screen

#     # Click following button
#     following_button = try_for_element("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a", xpath)
#     following_button.click()

#     # Empty list of following
#     following = []

#     # Modal for window of following
#     following_panel = try_for_element('div[role=\'dialog\'] ul', css)  # unordered list of following

#     loaded_following = following_panel.find_elements_by_css_selector('li')  # list of followers loaded from the list
#     loaded_following_till_now = len(loaded_following)

#     # Action chains
#     actions = ActionChains(driver)
#     actions.move_to_element(following_panel)
#     actions.click()
#     actions.perform()
#     actions.reset_actions()

#     index = 1

#     items = following_panel.find_elements_by_css_selector("ul span a")

#     for elem in items:
#         account_name = elem.text
#         following.append(account_name)
#         index += 1

#     # Message to user
#     print("Retrieving following list...\n")

#     # while loaded_till_now is less than the number of followers scroll and load more, populating loaded_following list
#     while loaded_following_till_now < int(following_number.text):
#         # Scroll modal window
#         actions.send_keys(Keys.END)
#         actions.perform()

#         loaded_following = following_panel.find_elements_by_css_selector("ul span a")
#         loaded_following_till_now = len(loaded_following)

#         for elem in loaded_following[index:loaded_following_till_now]:
#             account_name = elem.text
#             following.append(account_name)
#             index += 1

#         actions.move_to_element(following_panel)

#     exit_button = try_for_element(
#         "body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > button", css)
#     exit_button.click()
#     print(following, len(following))

#     # Timer
#     print("\nTime of second loop... %s seconds\n" % (time.time() - start_time))

#     return following


# #   Compare the two lists and print out the result list
# followers = get_followers()
# following = get_following()

# users_who_dont_follow_you_back = set(following) - set(followers)
# users_who_you_dont_follow_back = set(followers) - set(following)

# dont_follow_you = sorted(users_who_dont_follow_you_back, key=str.lower)
# dont_follow_them = sorted(users_who_you_dont_follow_back, key=str.lower)

# print("Users who dont follow you:\n")
# print(dont_follow_you)
# print("\nUsers who YOU dont follow:\n")
# print(dont_follow_them)


# def write_to_output():
#     with open("output.txt", 'w') as output:
#         output.write("Last checked:" + str(datetime.now()) + "\n\n")

#         output.write("Users who dont follow you back:" + "\n\n")
#         output.write(str("\n".join(dont_follow_you)) + "\n\n")

#         output.write("Users who YOU dont follow back:" + "\n\n")

#         output.write(str('\n'.join(dont_follow_you)))
#     output.close()


# write_to_output()

# driver.quit()
