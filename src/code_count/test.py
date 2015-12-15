#!/usr/bin/python
# coding:utf-8


from code_count import *


def test():
    cc = CodeCount()
    # cc.count_lines_r(['.', 'py'])
    cc.count_lines_r(['/home/gjz/Projects/caffe', 'h', 'cpp'])


def main():
    test()

if __name__ == '__main__':
    main()
