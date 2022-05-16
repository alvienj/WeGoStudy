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

def courseinformation():
    driver.find_element(By.XPATH, "//*[@id='student_list']/div[19]/div[3]/a[2]").click()
    sleep(1)
    driver.find_element(By.XPATH, "//span[text()='Select School']").click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="admission_institute_detail_id_chosen"]/div/div/input').send_keys('Douglas College')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="admission_institute_detail_id_chosen"]/div/ul/li/em').click()
    sleep(1)
    driver.find_element(By.XPATH, "//span[text()='Select Course']").click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="admission_institute_program_id_chosen"]/div/div/input').send_keys('Theatre Diploma')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="admission_institute_program_id_chosen"]/div/ul/li').click()
    sleep(1)
    driver.find_element(By.XPATH, "//span[text()='Select Starting Semester']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_starting_semester_chosen']//*[contains(@class, 'chosen-search-input')]").send_keys('1')
    sleep(1)
    driver.find_element(By.XPATH, "//li[text()='st']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//span[text()='Select Start Day']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_start_day_chosen']//*[contains(@class, 'chosen-search-input')]").send_keys('September')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="admission_start_day_chosen"]/div/ul/li').click()
    sleep(1)
    driver.find_element(By.XPATH, "//span[text()='Select Year']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_start_year_chosen']//*[contains(@class, 'chosen-search-input')]").send_keys('2022')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="admission_start_year_chosen"]/div/ul/li').click()

def personalinformation():
    driver.find_element(By.XPATH, "//*[@id='admission_middle_name']").send_keys(locators.firstname)
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_cambrian_id']").send_keys('12345')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_study_permit_number']").send_keys('12345')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_first_language']").send_keys('English')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_country_of_citizenship_chosen']//span[text()='Canada']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_country_of_citizenship_chosen']//*[contains(@class, 'chosen-search-input')]").send_keys('Canada')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="admission_country_of_citizenship_chosen"]/div/ul/li').click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_date_of_admission']").send_keys('1')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_gender_male']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_stay_type_private_residence']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_address_attributes_apartment_number']").send_keys('100')

def englishscores():
    driver.find_element(By.XPATH, "//*[@id='admission_english_score_attributes_overall_band']").send_keys('100')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_english_score_attributes_listening']").send_keys('100')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_english_score_attributes_reading']").send_keys('100')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_english_score_attributes_writing']").send_keys('100')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_english_score_attributes_speaking']").send_keys('100')
    sleep(1)

def workexperience():
    driver.find_element(By.XPATH, "//*[@id='admission_work_experiences_attributes_0_type_of_industry']").send_keys('IT')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_work_experiences_attributes_0_position_rank']").send_keys('1')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_work_experiences_attributes_0_employer']").send_keys('WeGoStudy')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_work_experiences_attributes_0_title']").send_keys('Hello everyone')
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='admission_work_experiences_attributes_0_job_description']").send_keys(locators.message)
    sleep(1)
    driver.find_element(By.XPATH, "//*[@name='commit']").click()

def Teardown1():
    if driver is not None:
        print(f'Test Started at: {datetime.datetime.now()}')
        print(f'--------------------------------------')

def Teardown2():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
    driver.close()
    driver.quit()



Teardown1()
Setup()
login()
students()
courseinformation()
personalinformation()
englishscores()
workexperience()
Teardown2()