#coding=utf-8
from selenium import webdriver
from time import sleep
#调Chrome驱动
a= webdriver.Chrome()
#调网址
a.get("http://119.3.71.63:8030/workLog/login")
sleep(2)

print 'Before login==========='
#打印当前页面title
title = a.title
print title
#打印当前页面URL
now_url = a.current_url
print now_url

#通过class属性打印元素的尺寸
b = a.find_element_by_class_name('form-control').size
print b
#打印通过一个元素的type获取另一个元素的class
c =a.find_element_by_xpath("//input[@type='password']").get_attribute('class')
print c
#打印该路径下元素的文字
d =a.find_element_by_xpath('/html/body/div/div[2]/div[3]/button').text
print d
#判断class元素是否存在
c =a.find_element_by_class_name('form-control').is_displayed()
print c
for c in range(5):
	c =a.find_element_by_class_name('form-control').is_displayed()
	if c=='True':
		a.find_element_by_class_name('form-control').send_keys('wyk')
	else:
		sleep(1)
#清空class元素值
a.find_element_by_class_name('form-control').clear()
#在class元素下输入wyk
a.find_element_by_class_name('form-control').send_keys('wyk')
#清空该路径下元素值
a.find_element_by_xpath("//input[@type='password']").clear()
#在该路径下输入wyk
a.find_element_by_xpath("//input[@type='password']").send_keys('wyk')
#点击该路径下的元素
a.find_element_by_xpath('/html/body/div/div[2]/div[3]/button').click()
sleep(3)

print 'After login==========='
#打印当前页面title
title = a.title
print title
if title==u'日志管理系统-日志':
	print 'login sucess!'
else:
	print 'login error!'	
#打印当前页面URL
now_url = a.current_url
print now_url
#判断是否登录成功
e = a.find_element_by_xpath("/html/body/div/aside/section/ul/li[2]/a/span").text
print e
if e==u'项目类型':
	print 'user login sucess!'
else:
	print 'user login error!'


