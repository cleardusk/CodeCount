# About
This is a simple tool for source code analysis, such as counting the total lines of source code (i.e. .c .cpp) in a specific directory. The small project arises of my interest, and I don't know where it goes.

# Usage
**Examples:** 

```
python count_lines.py ./src cpp

python count_lines.py ~/path/dir h hpp c cpp

$ python count_lines.py ~/Projects/caffe/ cpp c hpp h py m sh           
177601
```

**Attention**

The suffix name does not contain dot '.' .

**Module installation and usage**

Installation is easy, just type

```
$ python set_up.py install
```

And the example to use the module

```
>>> import count_lines
>>> count_lines.main('/home/gjz/Projects/caffe','cpp', 'c', 'h', 'hpp', 'm', 'sh')
149473
```

