#coding=utf-8
from selenium import webdriver
import time
#调Chrome驱动
a= webdriver.Chrome()
#调网址
a.get("http://101.132.154.156:8080/workLog/")
time.sleep(2)

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
		time.sleep(1)
#清空class元素值
a.find_element_by_class_name('form-control').clear()
#在class元素下输入wyk
a.find_element_by_class_name('form-control').send_keys('wyk')
#清空该路径下元素值
a.find_element_by_xpath("//input[@type='password']").clear()
#在该路径下输入wyk
a.find_element_by_xpath("//input[@type='password']").send_keys('wyk10240012.')
#点击该路径下的元素
a.find_element_by_xpath('/html/body/div/div[2]/div[3]/button').click()
time.sleep(3)

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


"""
    python中时间日期格式化符号：
    ------------------------------------
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称  # 乱码
    %% %号本身
"""
# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
import calendar
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
cal = calendar.month(2019, 3)
print "以下输出2019年3月份的日历:"
print cal