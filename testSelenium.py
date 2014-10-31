# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('http://google.com')
caja = driver.find_element_by_name('q')
caja.send_keys('ingsoftware uaz' + Keys.RETURN)
# driver.find_element_by_id('gbqfba').click()
time.sleep(3)
link = driver.find_element_by_link_text('Ingeniería de Software - UAZ')
link.click()
