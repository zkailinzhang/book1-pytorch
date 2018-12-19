#-*- coding:utf-8 -*-

from __future__ import print_function

class Foo(object):
    def __init__(self,func):
        self._func =func

    def __call__(self):
        print ('class decorator runing')

        self._func()

        print ('class decorator ending')

@Foo
def bar():
    print ('bar')


if __name__ == "__main__":
    bar()    
