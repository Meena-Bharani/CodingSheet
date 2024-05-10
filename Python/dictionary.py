
#  1. Adding a list as a dictionary's key
#####  dictionary1:
# _dict = {}
# _list = [1,2,3]
# _dict[_list] = 'Added'
# # Output
# _dict[_list] = 'Added'
# #TypeError: unhashable type: 'list'
#
# to overcome this error, follow the __hash__

class ClassList(list):
    def __hash__(self):
        return 0
_dict = {}
_list = ClassList([1,2,3])
_dict[_list] = 'Added'
print(_dict)

#output {[1,2,3]:'Added'}

####################################################################

# 2. using dictionary's as an Alternative to IF conditions

num=1
if num==1:
    funcA()
elif num==5:
    funcB()
else:
    func()

### can be written as

num =1

func_mapping = {1: funcA(), 2: funcB()}
func_mapping.get(num, func)() ## func is the default function

########################################

# 3. Dictionaries a switch statement
def switch_case(case):
    return {
        'case1' : 'This is case 1'
        ,'case2' : ' This is case 2'
        'default': 'This is default'
    }.get(case,'Invalid case')
result = switch_case('case1')

# output : this is case 1

#############################
# 4. __missing__ items

class MyDict(dict):
    def __missing__(selfself, key):
        self[key] = rv = []
        return rv
m = MyDict()
m['foo'].append(1)
m['foo'].append(2)

print(dict(m))   # {'foo': [1,2]}
print(m['x'])    # []

####  There is also a dict subclass in collections called 'defaultdict' that does pretty much the same but calls a function without arguments for not existing items.
# this can be useful when you want to provide a default value or perform a specific action when a key is not found, instead of raising a KeyError.
from collection import defaultdict

m= defaultdict(list)
m['foo'].append(1)
m['foo'].append(2)
print(dict(m))  #{'foo':[1,2]}

######################

#  5. hash equivalence key

my_dict = {'1':'string', True:'bool', 1:'int',1.0:float}
print(my_dict)

# output: {'1':'string', True: <class 'float'>}
#  dispite adding 4 distinct keys to a pythin dictionary, can you tell why it only preserves two of them ,
#  this is because - In python, dictionaries find a key based on the equivalence of hash (computed using hash()),
#  but not identity(computed using id()).
#  in this case there is no doubt that 1.0, 1 and True inherently have different datatypes and are also different objects.

print(id(1), id(True), id(1.0))
print(type(1), type(True), type(1.0))
# output : ##prints 3 different ids
#  <class 'int'> <class 'bool'> <class 'float'>

#  but the fact is they share the same hash value, the dictionary considers them as the same keys.
print(hash(1),hash(True),hash(1.0))
# output : 1 1 1
#  and also did you see the value corresponding to True is bool, but it prints float.
#  output: {'1':'string', True:<class 'float'>}
#  This is because at first, True is added as a key and its value is 'bool'. Next, while adding the key 1, python recognises it as an equivalent of the hash value.
#  Thus, the value correspond to True is overwritten by 'int', while the key (True) is kept as is.

# Finally while adding 1.0, another hash equivalence is encountered with an existing key of True.
#  yet again the value corresponding to True, which was updated to 'int' in the previous step,is overwritten by 'float'

###################################
#

