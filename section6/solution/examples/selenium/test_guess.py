import os
import pathlib
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


driver = webdriver.Chrome()
driver.get(file_uri("guess.html"))

# figure out what the number is
MIN_GUESS = 1
MAX_GUESS = 10000

# get the fields. These will come back regardless of whether the element is currently visible or not
input_tag = driver.find_element(By.ID, "guess")
won = driver.find_element(By.ID, "won")
feedback_div = driver.find_element(By.ID, "feedback")

while True:
    # We are still binary searching! But you could also have used a for loop
    guess = (MAX_GUESS + MIN_GUESS) // 2
    input_tag.send_keys(guess)
    input_tag.send_keys(Keys.ENTER)

    # check for won
    if won.is_displayed():
        print(f"The guess was {guess}")
        break

    # check for too high or too low
    feedback = feedback_div.find_element(By.TAG_NAME, "h3").text
    if feedback == "Too High":
        max_guess = guess - 1
    else:
        min_guess = guess + 1

driver.quit()
