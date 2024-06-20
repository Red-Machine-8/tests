import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(binary_path=binary_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://sbis.ru/")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.LINK_TEXT,'Контакты').click()
time.sleep(3)

elementSpan =driver.find_element(By.XPATH, "//span[contains(@class, 'sbis_ru-Region-Chooser__text sbis_ru-link')]")
if elementSpan.text == 'Ярославская обл.':
    print("Выбран верный регион")
elementPartn = driver.find_element(By.XPATH, "//div[contains(@class, 'viewContainer')]")
strPartn = elementPartn.text
if elementPartn:
    print("Есть список партнеров")
elementSpan.click()
driver.find_element(By.XPATH, "//span[contains(@title, 'Камчатский край')]").click()

if "Камчатский" in driver.find_element(By.XPATH, "//span[contains(@class, 'sbis_ru-Region-Chooser__text sbis_ru-link')]").text:
    print("Подставился выбранный регион")
if "Камчатский" in driver.title:
    print("Выбранный регион есть в title")
if "kamchatskij-kraj" in driver.current_url:
    print("Выбранный регион есть в url")
if strPartn != driver.find_element(By.XPATH, "//div[contains(@class, 'viewContainer')]").text:
    print("Список партнёров изменился")

driver.implicitly_wait(600)