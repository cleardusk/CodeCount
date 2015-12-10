#!/usr/bin/python
# coding:utf-8
'''
v0.1: count specific suffix files total lines, 2015.12.10:23:00~23:55
'''
import os
import sys

def main():
	if len(sys.argv) == 1:
		help()
	elif len(sys.argv) == 2:
		sys.argv.append('.m')
		count_lines(sys.argv[1:])
	else:
		count_lines(sys.argv[1:])

def help():
	print 'Usage: python count_lines.py dir_path suffix\n'
	print 'Example: python count_lines.py ./src .c .cpp'

def count_lines(argv):
	# print len(argv)
	# print argv
	total_lines = 0
	for file in os.listdir(argv[0]):
		# print file
		if file[file.rfind('.'):] in argv[1:]:
			file_path = os.path.join(argv[0], file)
			with open(file_path) as f:
				total_lines += 	f.read().count('\n')

			## simple implemention	
			# f = open(file)
			# scripts = f.read()
			# total_lines = total_lines + scripts.count('\n')
			# f.close()
	print total_lines

if __name__ == '__main__':
	main()
