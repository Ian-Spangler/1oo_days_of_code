# Capstone Project Data Entry Job Automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

class SFRentingResearch:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.address = []
        self.links = []
        self.prices = []

    def zillow_search(self):
        zillow_response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
        zillow_webpage = zillow_response.text
        soup = BeautifulSoup(zillow_webpage, "html.parser")
        all_items = soup.find_all(name = "a", class_="StyledPropertyCardDataArea-anchor")
        for item in all_items:
            self.address.append(item.find("address").getText().strip())
            self.links.append(item.get("href"))
        all_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
        for price in all_prices:
            self.prices.append(price.getText().split("/")[0].replace("+","").split(" ")[0])


    def auto_fill_form(self):
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd_X36pF2XUw1_hAEa4-moR7rCchuPxKrqi8wJIH9R1P_lOgQ/viewform?usp=header")
        for n in range(len(self.links)):
            responses = self.driver.find_elements(By.CSS_SELECTOR, value=".Xb9hP input")
            responses[0].send_keys(self.address[n])
            responses[1].send_keys(self.prices[n])
            responses[2].send_keys(self.links[n])
            submit = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            submit.send_keys(Keys.ENTER)
            time.sleep(0.5)
            next_form = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            next_form.send_keys(Keys.ENTER)
            time.sleep(0.5)


bot = SFRentingResearch()
bot.zillow_search()
bot.auto_fill_form()