from selenium import webdriver
import time
import json
import requests


with open("config.json","r") as f:
    params = json.load(f)

try:
    browser = webdriver.Chrome()
    browser.get(params['url'])
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/input').send_keys(params['name'])
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/input').send_keys(params['password'])
    browser.find_element_by_class_name('btn').click()
    time.sleep(5)
    browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div[4]/ul/li[7]/div/input').click()
    time.sleep(5)
    browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div[4]/ul/li[8]/div/div/div[4]').click()
    time.sleep(5)
    browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div[5]/div/a').click()
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="wapcf"]/div/div[2]/div[2]').click()
    time.sleep(5)
except Exception as e:
    url = 'https://sc.ftqq.com/%s.send?text=打卡失败&desp=%s'%(params['sckey'],e)
    requests.get(url)
    time.sleep(5)
else:
    url = 'https://sc.ftqq.com/%s.send?text=打卡成功'%params['sckey']
    requests.get(url)
    time.sleep(5)
finally:
    browser.quit()