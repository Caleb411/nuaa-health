from selenium import webdriver
import time
import json

with open("config.json","r") as f:
    params = json.load(f)

browser = webdriver.Chrome()
browser.get(params['url'])
browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/input').send_keys(params['name'])
browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/input').send_keys(params['password'])
browser.find_element_by_class_name('btn').click()
time.sleep(5)
browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div[4]/ul/li[7]/div/input').click()
time.sleep(5)
browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div[5]/div/a').click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="wapcf"]/div/div[2]/div[2]').click()
time.sleep(5)
browser.quit()