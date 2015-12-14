#!/usr/bin/python
# coding:utf-8
'''
v0.1: count specific suffix files total lines, 2015.12.10:23:00~23:55
v0.11: add a new function count_lines_r() to count lines of code *recursively*
'''
import os
import sys
from pprint import pprint


def help():
    print 'Usage: python count_lines.py dir_path suffix_names\n'
    print 'Example: python count_lines.py ./src c cpp'


def count_lines(argv):
    '''
    argv[0]: the directory
    argv[1:]: suffix names
    return: total lines of code in the directory
    '''

    total_lines = 0
    for file in os.listdir(argv[0]):
        # print file
        if file[file.rfind('.') + 1:] in argv[1:]:
            file_path = os.path.join(argv[0], file)
            with open(file_path) as f:
                total_lines += f.read().count('\n')

            # simple implemention
            # f = open(file)
            # scripts = f.read()
            # total_lines = total_lines + scripts.count('\n')
            # f.close()

    return total_lines


def walk_dir(dr_path='.', files_container=[]):
    if os.path.isfile(dr_path):
        files_container.append(dr_path)
    elif os.path.isdir(dr_path):
        for dr in os.listdir(dr_path):
            walk_dir(os.path.join(dr_path, dr), files_container)
    else:
        pass


def count_lines_r(argv):
    '''
    argv[0]: the directory
    argv[1:]: suffix names
    return: total lines of code in the directory
    '''
    files_container = []
    walk_dir(argv[0], files_container)

    total_lines = 0
    for fl_path in files_container:
        if fl_path[fl_path.rfind('.') + 1:] in argv[1:]:
            with open(fl_path) as f:
                total_lines += f.read().count('\n')

    return total_lines


def test():
    dr_stack = []
    walk_dir(dr_path='.', files_container=dr_stack)
    pprint(dr_stack)


def main_console():
    DEFAULT_SUFFIX_NAME = 'py'
    if len(sys.argv) == 1:
        help()
        return
    elif len(sys.argv) == 2:
        sys.argv.append(DEFAULT_SUFFIX_NAME)
    sys.argv[1] = os.path.expanduser(sys.argv[1])
    print count_lines_r(sys.argv[1:])


def main(*args):
    argv = []
    argv.extend(args)
    DEFAULT_SUFFIX_NAME = 'py'

    if len(argv) == 0:
        help()
    elif len(argv) == 1:
        argv.append(DEFAULT_SUFFIX_NAME)
        print count_lines_r(argv)
    else:
        print count_lines_r(argv)

if __name__ == '__main__':
    # main_console()
    # main('.')
    main_console()
    # test()
