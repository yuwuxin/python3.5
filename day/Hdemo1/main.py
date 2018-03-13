# _*_ coding: utf8 _*_
#!/usr/bin/python3

#打开一个文件
f = open('file.txt', 'w', encoding='utf8')

f.write('Python 是一个非常好的语言。\n是的，的确非常好!!\n')

#关闭打开的文件
f.close()


#读取一个文件
w = open('file.txt', 'r+', encoding='utf8')

v = w.read()

print(v)

v1 = w.readline()

print(v1)

w.close()