import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

time.sleep(1)

kw = driver.find_element(By.CSS_SELECTOR, '#kw')
kw.send_keys('python')

su = driver.find_element(By.CSS_SELECTOR, '#su')
su.click()
