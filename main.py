from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time

chrome_web_driver = "C:\Developement\chromedriver.exe"
INSTAGRAM_URL = "https://www.instagram.com/"
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
instagram_duplicate = "python"


class InstaFollower:

    def __init__(self):
        service = Service(executable_path=chrome_web_driver)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=service)
        self.driver.maximize_window()

    def login(self):
        time.sleep(6)
        self.driver.get(url=INSTAGRAM_URL)
        self.driver.find_element(By.NAME, "username").send_keys(EMAIL)
        self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(3)

    def find_followers(self):
        time.sleep(5 )
        search_instagram = self.driver.find_element(By.CLASS_NAME, "_aacl")
        search_instagram.click()
        time.sleep(5)
        not_now = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_wM"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        not_now.click()
        time.sleep(5)
        input_instagram_name = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_1R"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
        input_instagram_name.send_keys(instagram_duplicate)
        time.sleep(3)
        search_instagram.send_keys(Keys.DOWN)
        search_instagram.send_keys(Keys.ENTER)

    def follow(self):
        pop_up_window = self.driver.find_element(By.CLASS_NAME, "_aacl")
        get_followers_list = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")
        have_follower = True
        i = 0
        while have_follower:
            if get_followers_list[i].text == "Follow":
                get_followers_list[i].click()
                time.sleep(1)
            i += 1
            if i == len(get_followers_list) - 1:
                self.driver.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                    pop_up_window
                )
                get_followers_list = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")


def main():
    follow = InstaFollower()
    follow.login()
    follow.find_followers()
    follow.follow()


if __name__ == "__main__":
    main()


