# About
This is a simple tool for source code analysis, such as counting the total lines of source code (i.e. .c .cpp) in a specific directory. The small project arises of my interest, and I don't know where it goes.

# Usage

**Examples**

```
$ python code_count.py ~/Projects/caffe/ cpp c hpp h py m sh           
cpp  :   47320
c    :       0
hpp  :   15558
h    :   84970
py   :   28128
m    :     910
sh   :     715
total:  177601
```

Installation is easy, just type

```
$ python set_up.py install
```

And the example to use the module

```
>>> from code_count import code_count
>>> code_count.main('/home/gjz/Projects/')
py   :  926956
h    :  990047
cpp  :  862688
m    :   72310
total: 2852001
```

**The easiest way is to use it is in shell, it's wonderful!!!**

The shell command is **code-count**

```
$ code-count ~/Projects/caffe
py   :   28128
h    :   84970
cpp  :   47320
m    :     910
total:  161328
```