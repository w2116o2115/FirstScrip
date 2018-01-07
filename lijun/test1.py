#coding=utf-8
from selenium import webdriver

driver = webdriver.Firefox(executable_path = '/Users/lijun/work/geckodriver')
url='http://www.baidu.com'
driver.get(url)