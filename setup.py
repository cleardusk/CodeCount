#!usr/bin/python

# from distutils.core import setup
import os
from setuptools import setup
from setuptools import find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='code-count',
    version='0.1',
    long_description=read('README.md'),
    author='cleardusk',
    author_email='guojianzhu1994@foxmail.com',
    license='MIT',

    # py_modules=['count_lines']
    # packages=['count_lines']

    # find packages
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': 'code-count=code_count.count_lines:main_console'
    }
)
