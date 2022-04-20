##
import datetime
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from faker import Faker

wegostudy_url = "http://34.233.225.85/"
wegostudy_username = "yupenghe"
wegostudy_password = "Hyp.123123"

# generate the fake data
fake = Faker(locale="en_CA")
new_username = fake.user_name()
new_password = fake.password()
new_firstname = fake.first_name()
new_lastname = fake.last_name()
email_address = fake.email()

city = fake.city()
# country = fake.current.country()
description = fake.sentence(nb_words=60)
pic_description = fake.name()
list_of_interests = ["python", "Java", "C#"]
web_page_url = fake.url()
icq_number = fake.pyint(10000, 99999)
institution = fake.lexify(text='????????')
phone_number1 = fake.phone_number()
phone_number2 = fake.phone_number()
department = fake.lexify(text='??????')
address = fake.address().replace("\n", ", ")


# driver = webdriver.Chrome("chromedriver.exe")
driver = webdriver.Chrome()


def setup():
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url=wegostudy_url)
    if driver.current_url == wegostudy_url and driver.title == "WeGoStudy":
        print(f"We are at WeGoStudy homepage:{driver.current_url}")
        print(f"We are seeing title message:{driver.title}")
    else:
        print("We are not at WeGoStudy homepage,please check your code.")
    assert driver.current_url == wegostudy_url


def teardown():
    if driver is not None:
        print("-----------------------------------------")
        print(f"Test is completed at:{datetime.datetime.now()}")
        driver.quit()


def check_featured_institutions():
    driver.find_element(By.LINK_TEXT, "BROWSE INSTITUTIONS").click()
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    institutions = driver.find_elements(By.XPATH, "//*[@class='col-12 col-lg-4 col-md-6']")
    for i in range(len(institutions)):
        try:
            college_name = institutions[i].find_element(By.TAG_NAME, "h4").text
            institutions[i].find_element(By.LINK_TEXT, "Visit Website").click()
            windows = driver.window_handles
            driver.switch_to.window(windows[-1])
            sleep(1)
            driver.close()
            driver.switch_to.window(windows[0])

            institutions[i].find_element(By.LINK_TEXT, "More").click()
            sleep(1)
            driver.back()
            sleep(1)
            institutions = driver.find_elements(By.XPATH, "//*[@class='col-12 col-lg-4 col-md-6']")

        except:
            print(f"Something error when visit:{college_name}")

    pass


def logger():
    old_instance = sys.stdout
    log_file = open('message.log', 'a')
    sys.stdout = log_file
    print(f"new user name:{new_username}, new password:{new_password}, email:{email_address}")
    sys.stdout = old_instance
    log_file.close()


if __name__ == '__main__':

    # logger()
    setup()
    check_featured_institutions()
    teardown()
