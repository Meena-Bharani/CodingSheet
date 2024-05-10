from collections import defaultdict
from functools import reduce

def countFreq(arr):
     f = defaultdict(int)
     for i in arr:
             f[i] += 1
     for k,v in f.items():
             print(k,v)

def decorator_ex1():
    pass

def add_list(*args):
    tot = 0
    xx = functools.reduce(lambda a,b: a+b , args)
    print('functools.reduce: ',xx)
    for i in args:
        tot += int(i)
    print(f'Sum: ',tot)
    return tot

def multi_list(*args):
    tot =0
    tot = args[0] * args[1]
    print('multi: ',tot)
    return tot

if __name__ == "__main__":
    arr = [1, 2, 3, 3, 4, 5, 5, 5]
    # countFreq(arr)
    inp = input('Enter list: ')
    args = list(map(int,inp.strip('[]').split(',')))
    add_list(args)