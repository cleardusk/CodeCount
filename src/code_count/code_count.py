#!/usr/bin/python
# coding:utf-8
"""
This small project starts at *2015.12.10:23:00*
v0.1: count code lines in specific directory
v0.11: add feature: specific directory --> directory and subdirectory
v0.12: wrapper it into a class
"""
import os
import sys


class CodeCount(object):
    """docstring for CodeCount"""
    def __init__(self):
        self.files_container = []  # store all the valid files path

    def help():
        print 'Usage: python count_lines.py dir_path suffix_names\n'
        print 'Example: python count_lines.py ./src c cpp'

    def walk_dir(self, dr_path='.'):
        """scan the valid files recursively, it's deeply first,
        files_container behavours like a stack"""

        if os.path.isfile(dr_path):
            self.files_container.append(dr_path)
        elif os.path.isdir(dr_path):
            for dr in os.listdir(dr_path):
                self.walk_dir(os.path.join(dr_path, dr))
        else:
            pass

    def count_lines(self, arg):
        """
        arg[0]: the directory
        arg[1:]: suffix names, list
        return: total lines of code in the *current directory!*
        """

        total_lines = 0
        for valid_file in os.listdir(arg[0]):
            # print file
            if valid_file[valid_file.rfind('.') + 1:] in arg[1:]:
                file_path = os.path.join(arg[0], valid_file)
                with open(file_path) as f:
                    total_lines += f.read().count('\n')

        return total_lines

    def count_lines_r(self, arg):
        '''
        arg[0]: the directory
        arg[1:]: suffix names
        return: total lines of code in the *directory and subdirectory!*
        '''

        if len(arg) < 2:
            raise IOError('At least two parameters, the first one must be a directory')
            return None

        self.walk_dir(arg[0])

        total_lines = 0  # total lines
        suffix_names = arg[1:]
        spec_suffix_lines = [0 for i in suffix_names]  # all suffix file names
        for fl_path in self.files_container:
            suffix_name = fl_path[fl_path.rfind('.') + 1:]
            if suffix_name in suffix_names:
                with open(fl_path) as f:
                    lines = f.read().count('\n')
                    spec_suffix_lines[suffix_names.index(suffix_name)] += lines
                    total_lines += lines
        # for i in xrange(0, len(suffix_names)):
        #     print '%s: %s' % (suffix_names[i], spec_suffix_lines[i])
        # print 'total: %d' % total_lines
        for i in xrange(0, len(suffix_names)):
            print '{0:5}: {1:7d}'.format(suffix_names[i], spec_suffix_lines[i])
        print '{0:5}: {1:7d}'.format('total', total_lines)


def main_console():
    codecount = CodeCount()
    DEFAULT_SUFFIX_NAME = 'py'

    if len(sys.argv) == 1:
        help()
        return
    elif len(sys.argv) == 2:
        sys.argv.append(DEFAULT_SUFFIX_NAME)
    sys.argv[1] = os.path.expanduser(sys.argv[1])

    codecount.count_lines_r(sys.argv[1:])

if __name__ == '__main__':
    main_console()
    # test()
