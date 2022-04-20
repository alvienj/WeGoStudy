from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import locators as locators
from time import sleep
import datetime

s = Service('C:/Users/User/PycharmProjects/si/WeGoStudy/chromedriver.exe')
driver = webdriver.Chrome(service=s)


driver.maximize_window()
driver.implicitly_wait(30)
driver.get(locators.wegostudy_url)


def Setup():
    if driver.current_url == locators.wegostudy_url and driver.title == 'WeGoStudy':
        print('Were at the WeGoStudy homepage')
    else:
        print('Wrong website. Please try again')
        driver.close()
        driver.quit()
    sleep(.5)

def clickable():
    driver.find_element(By.XPATH, '//*[@id="navbar-nav"]/ul/li[6]/a').click()
    if driver.current_url == locators.getintouch_url:
        print('GET IN TOUCH page is working')
    else:
        print('Wrong page. Please check your website')
    sleep(1)
    driver.find_element(By.NAME, 'first_name').send_keys(locators.firstname)
    sleep(1)
    driver.find_element(By.NAME, 'last_name').send_keys(locators.lastname)
    sleep(1)
    driver.find_element(By.NAME, 'email').send_keys(locators.email)
    sleep(1)
    Select(driver.find_element(By.NAME, 'country')).select_by_visible_text('Canada')
    sleep(1)
    driver.find_element(By.NAME, 'city').send_keys(locators.city)
    sleep(1)
    driver.find_element(By.NAME, 'Message').send_keys(locators.message)
    sleep(1)
    driver.find_element(By.XPATH, "//*[contains(@class, 'agile-form-inlinecheckboxes')]//*[contains(@class, 'agile-field')]/div[3]/label/i").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[contains(@class, 'agile-form-inlineradios')]//*[contains(@class, 'i-checks')]/i").click()
    sleep(1)
    driver.find_element(By.XPATH, "//button[text()='SUBMIT']").click()
    sleep(1)
    if driver.current_url == 'http://34.233.225.85/thank-you-for-contacting-us':
        print('You have successfully submitted a question. Good job!')
    else:
        print('You are at the wrong page. Please try again')


def Teardown1():
    if driver is not None:
        print(f'Test Started at: {datetime.datetime.now()}')
        print(f'--------------------------------------')

def Teardown2():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')



Teardown1()
Setup()
clickable()
Teardown2()





