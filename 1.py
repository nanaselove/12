# #!/usr/bin/python
# # coding=UTF-8
# def printme ( str ):
#    "打印传入的字符串到标准显示设备上"
#    print str
#    return 
# printme ("我要调用用户自定义函数!");
# printme ("再次调用同一函数");

 
# #可写函数说明
# def printinfo( name, age ):
#    "打印任何传入的字符串"
#    print "Name: ", name;
#    print "Age ", age;
#    return;
 
# #调用printinfo函数
# printinfo( age=22, name="wyk" );

 
# #可写函数说明
# def printinfo( name, age = 35 ):
#    "打印任何传入的字符串"
#    print "Name: ", name;
#    print "Age ", age;
#    return;
 
# #调用printinfo函数
# printinfo( age=50, name="miki" );
# printinfo( name="wyk" );

# # 可写函数说明
# def sum( arg1, arg2 ):
#    # 返回2个参数的和."
#    total = arg1 + arg2
#    print "函数内 : ", total
#    return total;
 
# # 调用sum函数
# total = sum( 10, 20 );

# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
 
total = 0; # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2; # total在这里是局部变量.
   print "函数内是局部变量 : ", total
   return total;
 
#调用sum函数
sum( 10, 20 );
print "函数外是全局变量 : ", total


# c=0
# def sum(a,b):
# 	c = a*b;
# 	print c;
# sum( 20, 20 );
# print c


#!/usr/bin/python
# -*- coding: UTF-8 -*-


str = input("请输入：[x*5 for x in range(2,10,2)]")
print "你输入的内容是: ", str
