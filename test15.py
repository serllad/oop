import argparse
parser = argparse.ArgumentParser(description='This is a test')
parser.add_argument('echo')     # add_argument()指定程序可以接受的命令行选项
args = parser.parse_args()      # parse_args()从指定的选项中返回一些数据
print(args.__contains__('echo'))
print(type(args))