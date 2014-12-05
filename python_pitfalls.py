# inspired by "Top 10 Mistakes that Python Programmers Make" by Martin
# Chikilian, available at
# http://www.toptal.com/python/top-10-mistakes-that-python-programmers-make
#
# More Resources:
#   http://stackoverflow.com/questions/1011431
#   http://stackoverflow.com/questions/530530
#   https://wiki.python.org/moin/PythonWarts

# Mutable Function Defaults

def foo(bar=[]):        
    bar.append("baz")    
    return bar


'''
>>> foo()
["baz"]
>>> foo()
["baz", "baz"]
>>> foo()
["baz", "baz", "baz"]
'''

'''
Explanation:

  "The default arguments value (list in this case) isn't instantiated
  the first time the function is called but rather at function
  definition time, i.e. the moment the containing scope of the
  function is executed."

 from reddit discussion
 http://www.reddit.com/r/programming/comments/251it6/

Workaround:

def foo(bar=None):
    if not bar:
        bar = []
    bar.append("baz")
    return bar
'''


# Class variable assignment

class A(object):
    x = 1

class B(object):
    pass

class C(object):
    pass


A.x, B.x, C.x
