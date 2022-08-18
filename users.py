#! /usr/bin/env python
# -*- coding: utf-8 -*-
#多用户登录

user_list={
    'u01':{'password':'123'},
    'u02':{'password':'123'},
    'u03':{'password':'123'},
}
f = open('blacklist.txt','r')
lock_file = f.readlines()
f.close()
count=0
while True:
    if count == 3:
        print("用户名输入次数到达3次限制")
        break
    user_name=input("请输入您的用户名>>：")
    if user_name not in user_list:
        print("用户名错误")
        count+=1
    if user_name in lock_file:
        print("用户名已锁定，请联系管理员！")
        exit()
    if user_name in user_list:
        user_password=input("请输入您的密码>>: ")
        if user_password == user_list[user_name]['password']:
            print("欢迎登录")
            break
        else:
            print("密码错误")
            count += 1
        if count == 3 :
            print("您输入的密码错误次数已达3次，将锁定您的用户！")
            f = open('blacklist.txt','w')
            f.write('%s'%user_name)
            f.close()
            break