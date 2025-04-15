import os
import pathlib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()
driver.get(file_uri("guess.html"))

# TODO: figure out what the number is
# These docs may be helpful https://www.selenium.dev/documentation/webdriver/getting_started/first_script/


driver.quit()
