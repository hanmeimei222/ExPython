# -*- coding: utf-8 -*-

# 有逗号，input参数紧接该句后面输入；没有逗号，input的参数另起一行输入
'''
# 输入 "abc" 或abc都可以
# 输入123 返回结果是str
print "How old are you?",
age = raw_input()
# How tall are you? 6'2" 转译输出'6\'2"'
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
'''
# test for input()：输入 "abc" 而不可以abc 
# 输入123 返回结果是int 
print "How old are you?",
age = input()
# How tall are you? 6'2" 转译输出'6\'2"'
print "How tall are you?",
height = input()
print "How much do you weigh?",
weight = input()


print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
# test for input 中文
print "So, you're %s old, %r tall and %s heavy." % (
    age, height, weight)
