## Two pointer(This is very imp pattern, not just for these probs but very commonly you can use this technique)

## Find pair with given sum
# {0, -1, 2, -3, 1}, x= -2    =>   yes ==> 1 + (-3) = -2
# {1, -2, 1, 0, 5}, x = 0     =>  no
def pair_given_sum(lst, x):
    try:
        pair = [(j,q) for i,j in enumerate(lst) for p,q in enumerate(lst[i+1:]) if j+q ==x]
        if len(pair) >0:
            print(f'The sum of the pair {pair} will give {x}')
            return pair
        print(f'No pair gives the sum {x}')
        return 0
    except Exception as e:
        raise Exception('Error: ',e)

## 3 sum
## array = {12, 3, 4, 1, 6, 9}, sum = 24 ; Output: 12, 3, 9
## array = {1, 2, 3, 4, 5}, sum = 9 ; Output: 5, 3, 1
def triplet_given_sum(lst, x):
    try:
        n=len(lst)
        pair = [(lst[i],lst[p],lst[y]) for i in range(0,n-2) for p in range(i+1,n-1) for y in range(p+1,n) if lst[i]+lst[p]+lst[y] == x]
        if len(pair) >0:
            print(f'The sum of the pair {pair} will give {x}')
            return pair
        print(f'No pair gives the sum {x}')
        return 0
    except Exception as e:
        raise Exception('Error: ',e)

## 4 sum
## array = {10, 2, 3, 4, 5, 9, 7, 8}, X = 23; Output: 3 5 7 8
##  array = {1, 2, 3, 4, 5, 9, 7, 8}, X = 16 ; Output: 1 3 5 7
def four_given_sum(lst, x):
    try:
        n=len(lst)
        pair = [(lst[i],lst[p],lst[y],lst[z]) for i in range(0,n-3) for p in range(i+1,n-2) for y in range(p+1,n-1) for z in range(y+1,n) if lst[i]+lst[p]+lst[y]+lst[z] == x]
        if len(pair) >0:
            print(f'The sum of the pair {pair} will give {x}')
            return pair
        print(f'No pair gives the sum {x}')
        return 0
    except Exception as e:
        raise Exception('Error: ',e)

## Find triplets with zero sum
def triplet_zero_sum(lst):
    try:
        n=len(lst)
        x=0
        pair = [(lst[i],lst[p],lst[y]) for i in range(0,n-2) for p in range(i+1,n-1) for y in range(p+1,n) if lst[i]+lst[p]+lst[y] == x]
        if len(pair) >0:
            print(f'The sum of the pairs {pair} will give {x}')
            return pair
        print(f'No pair gives the sum {x}')
        return 0
    except Exception as e:
        raise Exception('Error: ',e)

## Count Triplets such that one of the numbers can be written as sum of the other two
# Input : A[] = {1, 2, 3, 4, 5}  Output : 4
# The valid triplets are:  (1, 2, 3), (1, 3, 4), (1, 4, 5), (2, 3, 5)
def triplet_two_sum_as_third(lst):
    try:
        n=len(lst)
        x=0
        pair = [(lst[i],lst[p],lst[y]) for i in range(0,n-2) for p in range(i+1,n-1) for y in range(p+1,n) if lst[i]+lst[p]==lst[y]]
        if len(pair) >0:
            print(f'The sum of the two numbers in the pair {pair} will give third as result')
            return pair
        print(f'No pair doesnt gives the sum of third as a result')
        return 0
    except Exception as e:
        raise Exception('Error: ',e)

## Union of two arrays(Learn the brute force & optimal soln, you will learn about set datastructure, which will be super useful in many probs in brute force)
def union_two_array(lst1,lst2):
    try:
        # return set(lst1+lst2)  ## union
        lst1 = sorted(lst1)
        lst2 = sorted(lst2)
        final_list =[]
        x,y = 0,0
        while x < len(lst1) and y < len(lst2):
            if lst1[x] < lst2[y] and lst1[x] not in final_list:
                final_list.append(lst1[x])
                x += 1
            elif lst2[y] not in final_list:
                final_list.append(lst2[y])
                y += 1

        if x < len(lst1):
            if lst1[x] not in final_list:
                final_list.append(lst1[x])

        if y < len(lst2):
            if lst2[y] not in final_list:
                final_list.append(lst2[y])
        print(final_list)
        return final_list
    except Exception as e:
        raise Exception('Error: ',e)

## Intersection of two arrays(Learn the brute force & optimal soln, you will learn about set datastructure, which will be super useful in many probs in brute force)
def intersection_two_array(lst1,lst2):
    try:
        # return list(filter(lambda a: a in lst1, lst2))  ##intersection
        lst1 = sorted(lst1)
        lst2 = sorted(lst2)
        final_list =[]
        x,y = 0,0
        while x < len(lst1) and y < len(lst2):
            if lst1[x] < lst2[y]:
                x += 1
            elif lst[x] > lst2[y]:
                y += 1
            else:
                final_list.append(lst1[x])
                x += 1
                y += 1
        print(final_list)
        return final_list
    except Exception as e:
        raise Exception('Error: ',e)

## Remove duplicates from array(Quite diff from above, try to solve on own, this actually shows that not always you will have pointers at start and end)
def remove duplicates(lst):
    try:
        pass
    except Exception as e:
        raise Exception('Error: ',e)


# def pair_given_sum(lst, x):
#     try:
#         pass
#     except Exception as e:
#         raise Exception('Error: ',e)

## Find pair with given sum
if __name__ == '__main__':
    # n = int(input('Enter number of elements: '))
    # lst = []
    # for i in range(n):
    #     l = int(input(f'Enter number {i + 1} : '))
    #     lst.append(l)
    n = input('Enter List[]: ')
    lst = list(map(int,n.strip('[]').split(',')))

    ## Find pair with given sum
    # x = int(input('Enter number of elements: '))
    # pair_given_sum(lst,x)
    # triplet_given_sum(lst,x)
    # four_given_sum(lst,x)

    ## Find pair with given sum zero
    # triplet_zero_sum(lst)

    ## Count Triplets such that one of the numbers can be written as sum of the other two
    # triplet_two_sum_as_third(lst)

    ## Union of two arrays(Learn the brute force & optimal soln, you will learn about set datastructure, which will be super useful in many probs in brute force)
    # n1 = int(input('Enter number of elements: '))
    # lst1 = []
    # for i in range(n1):
    #     l = int(input(f'Enter number {i + 1} : '))
    #     lst1.append(l)
    # union_two_array(lst,lst1)

    ## Intersection of two arrays(Learn the brute force & optimal soln, you will learn about set datastructure, which will be super useful in many probs in brute force)
    # n1 = int(input('Enter number of elements: '))
    # lst1 = []
    # for i in range(n1):
    #     l = int(input(f'Enter number {i + 1} : '))
    #     lst1.append(l)

    n = input('Enter List[]: ')
    lst1 = list(map(int, n.strip('[]').split(',')))
    intersection_two_array(lst,lst1)