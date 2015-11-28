# -- coding: utf-8 --
# use ':%/my_//g' to remove all the prefix 'my_'
name = 'Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# exercise for "format string"
print "Let's talk about %s." % name
# 十进制 %d
print "He's %d years old." % age
# 十六进制 %x
print "He's %x years old." % age
# 八进制 %o
print "He's %o years old." % age
# 格式化输出浮点数
print "He's %f years old." % age
# 格式化输出浮点数（制定保留小数点位数）
print "He's %.3f years old." % age
# 指定占位符宽度
print "name:%10s, age:%8d, height:%8.2f" % (name, age, height)
# 制定占位符宽度（左对其）
print "name:%-10s, age:%-8d, height:%-8.2f" % (name, age, height)
# 制定占位符（0）
print "name:%-10s, age:%08d, height:%08.2f" % (name, age,height)
# 科学计数法
print "height:%.2e" % height
# 四舍五入
print round(1.7333)
# 英寸->厘米
print "He's %d inches tall." % height
print "He's %.2f cm tall." % float(height*2.54)
# 磅->千克
print "He's %d pounds heavy." % weight
print "He's %.2f kg heavy." % float(weight*0.4536)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
print "test for '%%r' my name is %r, I am %r years old, my eyes is %r" % (name, age, eyes)
