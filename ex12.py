# -*- coding:utf-8 -*-
#提示输入字符串可以作为raw_input("####")的参数来实现
#查看文档pydoc raw_input
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy. " % (
     age, height, weight)
