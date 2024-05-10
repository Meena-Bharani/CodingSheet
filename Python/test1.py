class FirstClass_C:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def get_first_val(self):
        cc = print(f'This will return first class values name {self.name} and age {self.age}')
        return cc
    
class FetchClass(FirstClass_C):
    def __init__(self,name,age):
        super().__init__(name,age)

    # @FirstClass_C.
    def fetch_values(self):
        super().get_first_val()
        sp_ex = print(f'sp exe values are here')
        return sp_ex

# class SecondClass_Q(FirstClass_C):
#     def __init__(self,type_name,**cm):
#         super().__init()
#         self.type_name = type_name
#         self.cm = tuple(cm.keys())
#         self.vl = tuple(vl.values())
    
#     # @get_first_val
#     def get_second_val(self):
#         it = print(f'This will return second class values {self.type_name} cm as follows {self.cm} vl as follows')
#         return it

c = FirstClass_C('aaa',10)
n=getattr(c,'name')
a=getattr(c,'age')

f = FetchClass(n,a)
f.fetch_values()

# s = SecondClass_Q('tname',c1=v1,c2=v2)
# s.get_second_val()


