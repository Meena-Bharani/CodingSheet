
def decorator_func(arg1,arg2):
    def actual_decorator(func):
        def wrapper(*args,**kwargs):
            print('**************')
            print(arg1,arg2)
            print(*args,**kwargs)
            print('--------------')
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator

@decorator_func('hello','world')
def greeting(name):
    print(f'Hey {name}')
    return f'Hey {name}'

greeting('Meena')

