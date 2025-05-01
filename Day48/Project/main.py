from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

start_time = time.time()

game_is_on = True

while game_is_on:
    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()

    store = driver.find_elements(By.ID, value="store")
    store = store[::-1]

    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time >= 5:
        start_time = time.time()
        for item in store:
            if item.get_attribute("class") != "greyed":
                item.click()

