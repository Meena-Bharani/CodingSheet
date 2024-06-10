from typing import Callable, Any

# def flatten(target):
#     for sub in target:
#         if isinstance(sub, list):
#             yield from flatten(sub)
#         else:
#             yield sub

# type Flatten = Callable[[list],list]  # python 3.12
# flatten: Flatten = lambda target: sum((flatten(sub) if isinstance(sub, list) else [sub] for sub in target) ,[])
flatten = lambda target: sum((flatten(sub) if isinstance(sub, list) else [sub] for sub in target) ,[])

nested_list: list[Any] = [1,[2,3],[[4],5],['A','dsf'],[[['Test'],'Finally'],6.78]]
print(nested_list)
print(flatten(nested_list))

# print(list(flatten(nested_list)))
