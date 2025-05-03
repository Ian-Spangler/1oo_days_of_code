from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.similar_account = "city_xtra"

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)
        email = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        email.send_keys("100daysofcodetestIan@gmail.com")
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password.send_keys("9s6sA,$RK&+ykJG")
        login = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[3]/button')
        login.click()
        time.sleep(10)
        # Due to instagram update, we need to type authentication.
        # So, auto login became a much difficult process.
        # It is impossible to continue from here.

    def find_followers(self):
        pass

    def follow(self):
        pass