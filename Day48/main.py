from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is {price_dollar}.{price_cents}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link)
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# for time in event_times:
#     print(time.text)

event_title = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# for title in event_title:
#     print(title.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": f"2025-{event_times[n].text}",
        "name": event_title[n].text
    }

print(events)

# driver.close() # Close the active tab
driver.quit() # Close the entire browser (all tabs)