import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os

current_file = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file)
chrome_options = Options()
prefs = {'download.default_directory' : str(current_directory)}
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('prefs', prefs)
service = Service(binary_path=binary_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://sbis.ru/")
driver.maximize_window()
time.sleep(3)

localload = driver.find_element(By.XPATH, "//a[contains(text(), 'Скачать локальные версии')]")
ActionChains(driver).scroll_to_element(localload).perform()
driver.execute_script("arguments[0].click();", localload)
time.sleep(3)

driver.find_element(By.XPATH, "//div[contains(text(), 'СБИС Плагин')]").click()
driver.find_element(By.XPATH, "//span[contains(text(), 'Windows')]").click()
driver.find_element(By.XPATH, "//a[contains(text(), 'Exe')]").click()
time.sleep(5)







