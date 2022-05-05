from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import locators as locators
from time import sleep
import datetime


s = Service("C:/Users/User/PycharmProjects/si/WeGoStudy/Vien's Scripts/chromedriver.exe")
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

def login():
    driver.find_element(By.XPATH, "//b[text()='LOGIN']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='user_email']").send_keys(locators.login)
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='user_password']").send_keys(locators.password)
    sleep(1)
    driver.find_element(By.XPATH, "//*[@name='commit']").click()
    sleep(1)
    if driver.current_url == 'http://34.233.225.85/partner/home':
        print('You are signed in as a Partner')
    else:
        print('Oh something is wrong.. please fix go back')

def students():
    driver.find_element(By.XPATH, "//*[contains(@class, 'navbar-nav')]/li/a/span").click()
    sleep(1)
    driver.find_element(By.XPATH, "//a[text()='Students']").click()
    sleep(1)
    if driver.current_url == 'http://34.233.225.85/partners/student_details':
        print('You are on the student page')
    else:
        print('You are at the wrong page. Please try again')
    sleep(1)
    driver.find_element(By.XPATH, "//a[text()='Create New Student']").click()
    sleep(1)

def Personal():
    driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_first_name']").send_keys(locators.firstname)
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_middle_name']").send_keys(locators.firstname)
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_last_name']").send_keys(locators.lastname)
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_birth_date']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_birth_date']").send_keys('1985-02-13')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_passport_number']").send_keys('12345')
    sleep(1)
    driver.find_element(By.XPATH, '//*[contains(@class, "select2-selection")]').click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[contains(@class, 'select2-search__field')]").send_keys('Canada')
    sleep(1)
    driver.find_element(By.XPATH, "//html/body/span/span/span[2]/ul/li").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='phone_number']").send_keys(locators.phone)
    sleep(1)

def Contact():
    driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_address_attributes_mailing_address']").send_keys(locators.address)
    sleep(1)
    driver.find_element(By.XPATH, "//span[text()='Country']").click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_country_chosen"]/div/div/input').send_keys('Canada')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_country_chosen"]/div/ul/li/em').click()
    sleep(1)
    driver.find_element(By.XPATH, "//span[text()='Province/State']").click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_state_chosen"]/div/div/input').send_keys('British Columbia')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_state_chosen"]/div/ul/li/em').click()
    sleep(1)
    driver.find_element(By.XPATH, "//span[text()='City']").click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]/div/div/input').send_keys('Kamloops')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]/div/ul/li/em').click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_address_attributes_zip_code']").send_keys(locators.postalcode)
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='user_email']").send_keys(locators.email)
    sleep(1)

def Education():
    driver.find_element(By.XPATH, "//span[text()='Credentials']").click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/div/input').send_keys('Certificate')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/ul/li').click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_user_educations_attributes_0_school_name']").send_keys('Random High School')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_user_educations_attributes_0_program']").send_keys('Computer Science')
    sleep(1)
    driver.find_element(By.XPATH, "//span[text()='GPA Scale']").click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div/div/input').send_keys('4')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div/ul/li').click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='user_student_detail_attributes_user_educations_attributes_0_gpa']").send_keys('4')
    sleep(1)

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
login()
students()
Personal()
Contact()
Education()
Teardown2()