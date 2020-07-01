from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"")
driver.get("")
time.sleep(5)
content =driver.fine_element_by_css_selector()

class TestU