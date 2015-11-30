# -*- coding: utf-8 -*-
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm\\ a \\ cat."

# both """or ''' is ok
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

'''
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
'''
print tabby_cat
print "%s" % tabby_cat
print "%r" % tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# test for different kinds of escape sequences
# 反斜杠
print "this is test for backslash(\\\\): \\"

# 单双引号
print "this is test for single/double quote(\\\'&\\\"):\n"
print "I am 6'2\" tall."
print 'I am 6\'2" tall.'

# 发出系统铃声
print "this is test for ASCII Bell(\\a): \a"

# 退格符
print "this is test for ASCII Backspace(\\b):"
print " How are you?\n"  # 有空格，\b使得当前的输出位置退一格
print " \bI am fine.\n\n"  # 即输出的起始位置左移一位

# 回车符\r使得当前输出位置回到本行开头
print "\tHow are you?"
print "\rI am fine.\n\n"

# mix:p a s  ki
print "note:\n  a s\ti\b\bk\rp\n"

# 垂直制表符\v 它的作用是让\v后面的字符从下一行开始输出且开始的列数为\v前一个字符所在列后面一列
print "this\v is\v test\v for \\v"

# \uxxxx \xhh \Uxxxxxxxx \ooo
print u"\u4f60\u597d"
print "\xe4\xbd\xa0\xe5\xa5\xbd"
print u"\U0002F80A\U0002F80A\U0002F80B\U0002F80C"
print "\101\102\103"


'''
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,
'''
