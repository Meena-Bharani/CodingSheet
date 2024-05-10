from functools import wraps
from typing import Any, Callable, TypeVar, ParamSpec
P = ParamSpec('P')
R = TypeVar('R')
def t2(func):
# def t2(*args,**kwa):
# def t2(func: Callable[P,R]) -> Callable[P,R]:
    @wraps(func)
    def inner(*args,**kwa):
        t = 'this is t2'
        j = [i for i in args]
        k_k = tuple(kwa.keys())
        k_v = tuple(kwa.values())
        print(t)
        print(j)
        print(k_k,k_v)
        return func(*args,**kwa)
    return inner

# @t2(*args,**kwa)
@t2
def t1(xx,*args,**kwa):
    t ='this is t1 - '
    print(t,xx)
    return t

t1('val',1,2,3,4,a=11,b=22,c=33)
# print(t)