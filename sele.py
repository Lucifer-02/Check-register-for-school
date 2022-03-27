from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from playsound import playsound
from time import sleep
import signal
import sys

# Cancel handle
def signal_handler(sig, frame):
    print('\nCancel dang ky hoc!')
    driver.quit()
    sys.exit(1)

# login to my account


def open_and_login(driver, userName, passWord):
    userName_ele = driver.find_element_by_id("LoginName")
    userName_ele.send_keys(userName)
    passWord_ele = driver.find_element_by_id("Password")
    passWord_ele.send_keys(passWord)
    passWord_ele.send_keys(Keys.RETURN)

# check subject status


def check_subject() -> bool:
    table = driver.find_element_by_class_name("table")
    lines = table.text.split('\n')

    compiler_subject = lines[1].split(" ")
    tongSV = compiler_subject[6]
    daDK = compiler_subject[7]

    print(compiler_subject)

    return tongSV != daDK


signal.signal(signal.SIGINT, signal_handler)

PATH = "/run/media/lucifer/STORAGE/DOWNLOAD/chromedriver_linux64/chromedriver"

options = webdriver.ChromeOptions()
#  options.add_argument("headless")
driver = webdriver.Chrome(executable_path=PATH, options=options)
driver.get("http://dangkyhoc.vnu.edu.vn/")

open_and_login(driver, "18020574", "viethoang153")

# go to subjects list page
driver.get("http://dangkyhoc.vnu.edu.vn/dang-ky-mon-hoc-nganh-1")

while True:
    print("hoang dep trai vl")
    #  if check_subject():
    #      playsound('alarm.mp3')
    sleep(2)
    driver.refresh()
