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
driver.maximize_window()
driver.get("https://sbis.ru/")

driver.find_element(By.LINK_TEXT,'Контакты').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,'a[title=\"tensor.ru\"]').click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])

elementP = driver.find_element(By.XPATH, "//p[text()='Сила в людях']/following::a[text()='Подробнее']")
ActionChains(driver).scroll_to_element(elementP).perform()
time.sleep(3)
driver.execute_script("arguments[0].click();", elementP)

get_url = driver.current_url
if get_url == "https://tensor.ru/about":
    print("Переходим по ссылке 'https://tensor.ru/about'")

elementDiv = driver.find_element(By.XPATH, "//div[contains(@class, 'tensor_ru-container tensor_ru-section tensor_ru-About__block3')]")
ActionChains(driver).scroll_to_element(elementDiv).perform()
elementsDiv = elementDiv.find_elements(By.XPATH,"descendant::div[contains(@class, 'tensor_ru-About__block3-image-wrapper')]")
if elementsDiv[0].size['height'] == elementsDiv[1].size['height'] == elementsDiv[2].size['height'] == elementsDiv[3].size['height'] and elementsDiv[0].size['width'] == elementsDiv[1].size['width'] == elementsDiv[2].size['width'] == elementsDiv[3].size['width']:
    print("Все изображения имеют одинаковый размер")

driver.implicitly_wait(600)