import time

from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

driver.get('http://localhost:8081/#/')

time.sleep(1)

txt_id = driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[1]/div/input')

btn_submit = driver.find_element_by_xpath('//*[@id="btnCheck"]')

txt_id.send_keys('1')

time.sleep(1)

btn_submit.click()

time.sleep(2)

permission = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/a')

assert permission.text == 'development'

time.sleep(10)

driver.quit()
