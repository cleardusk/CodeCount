#!usr/bin/python

# from distutils.core import setup
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='codecount',
    version='0.1',
    long_description=read('README.md'),
    author='cleardusk',
    author_email='guojianzhu1994@foxmail.com',
    license='MIT',

    py_modules=['count_lines']
    # packages=['count_lines']
)
