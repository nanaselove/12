#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time 
a= webdriver.Chrome()
a.get("http://www.baidu.com")
#鼠标右击
b=a.find_element_by_id('su')
ActionChains(a).context_click(b).perform()
time.sleep(3)
'''
#定位元素源位置
element = a.find_element_by_id('')
#定位元素要移动到的目标位置
target = a.find_element_by_id('')
#执行元素的拖放操作
ActionChains(a).drag(b).perf_and_drop(element,target).perform()
'''
'''
#鼠标悬停
b =a.find_element_by_xpath('//*[@id="u1"]/a[8]')
ActionChains(a).move_to_element(b).perform()
time.sleep(3)
a.find_element_by_link_text('搜索设置').click()
'''