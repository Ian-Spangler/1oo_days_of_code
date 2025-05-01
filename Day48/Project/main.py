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

affordable = 0

five_seconds = time.time() + 5
five_minutes = time.time() + 60*5

cookie = driver.find_element(By.ID, value="cookie")

store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
store_id = [item.get_attribute("id") for item in store]
store_id.pop(len(store_id) - 1)

while game_is_on:
    cookie.click()

    if time.time() >= five_seconds:
        five_seconds = time.time() + 5

        store_price = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
        store_price.pop(len(store_price) - 1)
        prices = [int(price.text.split("-")[1].replace(",", "")) for price in store_price]

        upgrade_dict = {}
        for n in range(len(store_id) - 1):
            upgrade_dict[prices[n]] = store_id[n]

        current_cookie = driver.find_element(By.ID, value="money").text
        if "," in current_cookie:
            money_element = current_cookie.replace(",", "")
        current_cookie = int(current_cookie)

        for price in prices:
            if price <= current_cookie:
                affordable = price
        driver.find_element(By.ID, value=upgrade_dict[affordable]).click()

    if time.time() >= five_minutes:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        five_minutes = time.time() + 60 * 5