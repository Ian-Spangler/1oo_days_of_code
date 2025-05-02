from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

cookie_quit = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/button')
cookie_quit.send_keys(Keys.ENTER)

login = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
login.send_keys(Keys.ENTER)

input_email = driver.find_element(By.CSS_SELECTOR, value="#username")
input_email.send_keys("100daysofcodetestIan@gmail.com")

input_password = driver.find_element(By.CSS_SELECTOR, value="#password")
input_password.send_keys("9s6sA,$RK&+ykJG")

login_button = driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container  button")
login_button.click()

jobs = driver.find_elements(
    By.CSS_SELECTOR,
    ".pIFnaYAbsCdVmPcdEnTafeObZRrShHvhLg li div div div div div div a"
) # This doesn't find all employers. I can't fix it

for job in jobs:
    try:
        job.send_keys(Keys.ENTER)
        easy_apply = driver.find_element(By.CSS_SELECTOR, value=".jobs-apply-button--top-card button")
        easy_apply.send_keys(Keys.ENTER)
        mobile_phone_number = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4199990101-9-phoneNumber-nationalNumber"]')
        mobile_phone_number.send_keys("01012341234")
        submit_button = driver.find_element(By.CSS_SELECTOR, value=".display-flex.justify-flex-end.ph5.pv4 button")
        submit_button.send_keys(Keys.ENTER)
    except NoSuchElementException:
        print("This application is too complex")


