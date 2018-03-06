
#python3 基本数据类型
print('python3 基本数据类型')

i = 123456
f = 1.205
s = 'string'

print(i)
print(f)
print(s)
print('---------------------------------------------------------------------------------')


print('多个变量赋值')
print('Python允许你同时为多个变量赋值。例如：')
a = b = c = 1

print(a)
print(b)
print(c)

print('您也可以为多个对象指定多个变量。例如：')
a,b,c = 1,2,'aaa'
print(a)
print(b)
print(c)

print('---------------------------------------------------------------------------------')

print('标准数据类型')
print('Python3 中有六个标准的数据类型')
print('''
    Number（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Sets（集合）
    Dictionary（字典）
        ''')
print('---------------------------------------------------------------------------------')

print('Number（数字）')
print('''
    Python3 支持 int、float、bool、complex（复数）。
    在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
    像大多数语言一样，数值类型的赋值和计算都是很直观的。
    内置的 type() 函数可以用来查询变量所指的对象类型。
    ''')
a,b,c,d = 1,1.1,True,4+3j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print('---------------------------------------------------------------------------------')

print('List(列表)')
list = ['abcd',789,2.36,'runoob',70.2]
tinylist = [123,'runoob']
print(list)
print(list[1:2])
print(list[1:])
print(tinylist *2 )
print(list + tinylist)
print('---------------------------------------------------------------------------------')

print('Tuple(元组)')
tuple = ('abcd',456,2.22,'tuple',70.2)
tinytuple = (123, 'runoob')
print(tuple)
print(tinytuple)
print('---------------------------------------------------------------------------------')

print('Set(集合)')
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)

if('Rose' in student) :
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abcdef')
b = set('def')
print(a)
print(a - b)
print(a | b)
print(a & b)
print('# a和b中不同时存在的元素')
print(a ^ b)

print('---------------------------------------------------------------------------------')

print('Dictionary（字典）')
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict)
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

print('---------------------------------------------------------------------------------')
