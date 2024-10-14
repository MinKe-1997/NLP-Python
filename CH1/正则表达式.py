# -*- coding = utf-8 -*-
# @Time:  上午11:11
# @Author: 闵柯
# @File: 正则表达式.py
# @Software: PyCharm

input = "自然语言处理很重要。12abc789"
import re
# 匹配所有的
patten = re.compile(r'')
print(re.findall(patten, input))
# 匹配指定字母
patten_1 = re.compile(r'[a-zA-Z]')
print(re.findall(patten_1, input))
# 匹配文本
patten_2 = re.compile(r'[^a-zA-Z]')
print(re.findall(patten_2, input))
# 匹配数字
patten_3 = re.compile(r'\d')
print(re.findall(patten_3, input))
# 匹配非数字
patten_4 = re.compile(r'\D')
print(re.findall(patten_4, input))
# 匹配字母和数字
patten_5 = re.compile(r'\w')
print(re.findall(patten_5, input))
# 匹配非字母和数字
patten_6 = re.compile(r'\W')
print(re.findall(patten_6, input))
# 匹配间隔符
patten_7 = re.compile(r'\s')
print(re.findall(patten_7, input))
# "*"0或多次匹配
patten_8 = re.compile(r'\d*')
print(re.findall(patten_8, input))
# "+"1次或多次匹配
patten_9 = re.compile(r'\d+')
print(re.findall(patten_9, input))
# "?"0次或者1次
patten_10 = re.compile(r'\d?')
print(re.findall(patten_10, input))
# 精准匹配和最小匹配{1,3}
patten_11 = re.compile(r'\d{3}')
print(re.findall(patten_11, input))

input_2 = '123自然语言处理'
patten_new = re.compile(r'\d{1, 3}')
match = re.match(patten_new, input_2)
# match.group()

'''
字符串的替换和修改
'''
patten_new = re.compile(r'\d')
# 字符串的替换
re.sub(patten_new,'数字', input_2)
# 返回替换的个数
re.subn(patten_new,'数字', input_2)
# 修改操作
re.subn(patten_new,'', input_2)
'''
对字符串进行切片
'''
input_3 = "自然语言处理123机器学习456深度学习"
patten_new = re.compile(r'\d+')
re.split(patten_new, input_3)

'''
命名组
'''
patten_new = re.compile(r'(?P<dota>\d+)(?P<lol>D+)')
m = re.search(patten_new,input_3)
# print(m.groups('dota'))

