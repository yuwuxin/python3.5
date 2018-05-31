from os.path import os

"""获取指定目录及其子目录下的 py 文件路径
说明：l 用于存储找到的 py 文件路径 get_py 函数，
递归查找并存储 py 文件路径于 l"""

l = []

def get_py_file(path, l):

    # 获取path目录下所有文件
    fileList = os.listdir(path)

    for filename in fileList:

        # 获取path与filename组合后的路径
        pathTmp = os.path.join(path, filename)

        if os.path.isdir(pathTmp):
            get_py_file(pathTmp, l)
        elif filename[-3:].upper()=='.PY':   #不是目录,则比较后缀名
            l.append(pathTmp)

path = input('请输入路径:').strip()

get_py_file(path, l)
print('在%s目录及其子目录下找到%d个py文件\n分别为：\n'%(path,len(l)))
for v in l:
    print(v+'\n')



