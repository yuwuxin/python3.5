# -*- coding: utf-8 -*-
print("编码")
print("# -*- coding: utf-8 -*-")
print('---------------------------------------------------------------------------------')

print('标识符')
print('第一个字符必须是字母表里面的字母或者下划线 _ ')
print('标识符的其它组成部分有、字母、数字、下划线')
print('标识符对大小写敏感')
print('---------------------------------------------------------------------------------')


print('关键字')
import keyword
print(keyword.kwlist)
print('---------------------------------------------------------------------------------')

print('注释')
print('单行注释以#开头 # xxx')

print("多行注释以多个# '''  \"\"\" ");
print('---------------------------------------------------------------------------------')

print('行与缩进')
print('python最具特色的就是使用缩进来表示代码块、 不想要使用({})')
print('缩进的空格是可变的 但是同一代码块的语句必须包含相同的缩进空格数')
print('if Ture:')
print('    print(\'True\')')
print('else:')
print('    print(\'False\')')
print('---------------------------------------------------------------------------------')

print('多行语句')
print('Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句')
print('在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)')
print('total = item_one + \
        item_two + \
        item_three')
print('---------------------------------------------------------------------------------')

print('数据类型')
print('python3中数据有四种类型： 整数、长整数、浮点数、复数')
print('整数， 如 1')
print('长整数 是比较大的整数')
print('浮点数 如 1.23、3E-2')
print('复数 如 1 + 2j、 1.1 + 2.2j')
print('---------------------------------------------------------------------------------')

print('字符串')
print('python中单引号和双引号使用完全相同')
print('使用三引号可以指定一个多行字符串')
print('转义符\\')
print('自然字符串、通过字符串前加r或者R 转义字符会被原样输出')
print(r'转义符\n')
print('python允许处理unicode 字符串前加u或者U ')
print(u'this is an unicode string')
print('字符串是不可变的')
print('按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。')
print('---------------------------------------------------------------------------------')

print('空行')
print('---------------------------------------------------------------------------------')

print('等待用户输入')
input('\n\n按下enter键后退出。')

print('同一行显示多条语句')
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
print('---------------------------------------------------------------------------------')

print('多个语句构成代码组')
print('''缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。''')
print('如下实例')
if 1 == 1 :
    print("1")
elif 1 <= 1:
    print("2")
else:
    print("0")

print('---------------------------------------------------------------------------------')

print('Print 输出')
print('print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：')

x = 'a'
y = 'b'
print('# 换行输出')
print( x )
print( y )

print('# 不换行输出')
print(x, end='')
print(y, end='')

print('---------------------------------------------------------------------------------')

print('import与form_import')
print('在 python 用 import 或者 from...import 来导入相应的模块。')
print('导入 sys 模块')

import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

print('导入 sys 模块的 argv,path 成员')
from sys import argv,path  # 导入特定的成员
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

print('---------------------------------------------------------------------------------')
