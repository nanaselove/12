#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
a= webdriver.Chrome()
a.get("http://www.baidu.com")
#在该元素下键盘输入值
a.find_element_by_id('kw').send_keys('seleniumm')
sleep(2)
#在该元素中键盘输入删除键
a.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
sleep(2)
#在该元素中键盘输入空格
a.find_element_by_id('kw').send_keys(Keys.SPACE)
#在该元素中键盘输入值
a.find_element_by_id('kw').send_keys(u'下载')
sleep(2)
#在该元素中键盘操作ctrl+a
a.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
sleep(2)
#在该元素中键盘操作ctrl+x
a.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
sleep(2)
#在该元素中键盘操作ctrl+v
a.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
sleep(2)
#在该元素中键盘输入回车键
a.find_element_by_id('kw').send_keys(Keys.ENTER)
sleep(2)
a.quit()