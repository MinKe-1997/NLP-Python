# -*- coding = utf-8 -*-
# @Time:  上午10:52
# @Author: 闵柯
# @File: Python字符串处理.py
# @Software: PyCharm

'''
去掉空格或特殊字符串
'''
input_str = ' 今天天气不错，挺风和日丽的 '
# 去除空格
input_str.strip()

# 去除尾部空格
input_str.rsplit()

# 去除头部空格
input_str.lstrip()
input_str_1 = 'AAA今天天气不错，挺风和日丽的AAA'
# 去除指定字符串A
input_str_1.strip('A')
# 去除尾部A
input_str_1.rstrip('A')
# 去除头部A
input_str_1.lstrip('A')
# 替换指定字符串
input_str_1.replace("今天", "昨天")

'''
查找操作
'''
input_str.find("今天")
'''
判断操作
'''
# 判断有没有字母
input_str.isalpha()
# 判断是否为数字
input_str.isdigit()
'''
字符串的分割和合并操作
'''
# 以空格为准进行分割
input_str.split(' ')
# 合并字符串
''.join(input_str)
