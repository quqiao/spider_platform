import os
import time

files = 'F:\django\spider_platform\DataAnalysis\data\medical_data_20201109.xlsx'
# print(os.path.basename(files))  # 返回文件名
# print(os.path.dirname(files))  # 返回目录路径
# print(os.path.split(files))  # 分割文件名和目录
# print(os.path.join('test', 'test01', 'test02.txt'))  # 将目录和文件名合成一个路径

print(os.path.getatime(files))  # 输出最近访问时间
print(os.path.getctime(files))  # 输出文件创建时间
print(os.path.getmtime(files))  # 输出最近修改时间
print(time.gmtime(os.path.getmtime(files)))  # 以struct_time形式输出最近修改时间
print(os.path.getsize(files))  # 输出文件大小
print(os.path.abspath(files))  # 输出绝对路径
print(os.path.normpath(files))  # 规范path字符串形式


