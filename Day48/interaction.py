from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# n_of_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# print(n_of_articles.text)

# n_of_articles = driver.find_elements(By.CSS_SELECTOR, value='#articlecount ul li')
# print(n_of_articles[1].text.split()[0])

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Ian")

l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Park")

email = driver.find_element(By.NAME, value="email")
email.send_keys("100daysofcodetestIan@gmail.com")

button = driver.find_element(By.TAG_NAME, value="button")
# button.send_keys(Keys.ENTER)
button.click()