# Find the maximum and minimum element in array(After solving the search , you can solve all probs in this basics by
# yourself)
def max_min_array(lst: [int]):
    """

    :type lst: list
    """
    try:
        # m = sorted(lst)
        # print('min = {0} , max = {1}'.format(m[0],m[len(m)-1]))
        # return
        maxNum = minNum = None
        for i in lst:
            i = int(i)
            if minNum is None and maxNum is None:
                minNum = maxNum = i
            elif minNum > i:
                minNum = i
            elif maxNum < i:
                maxNum = i
        print(f'min = {minNum} , max = {maxNum}')
        return
    except Exception as e:
        raise Exception('Error: ', e)


# Sorting the list
def sorting_array(lst):
    try:
        for i, j in enumerate(lst):
            if i == len(lst) - 1:
                break
            for p, q in enumerate(lst[i + 1:], i + 1):
                if lst[i] > lst[p]:
                    lst[i], lst[p] = lst[p], lst[i]
        return lst
    except Exception as e:
        raise Exception('Error: ', e)


# Find third largest element in array
def third_largest(lst):
    try:
        # m = sorted(lst)
        # print('Third largest is {0}',format(m[2]))
        # return
        ##### or ####
        sorted_lst = sorting_array(lst)
        if len(sorted_lst) > 2:
            print(f'Third largest element in array is {sorted_lst[2]}')
            return sorted_lst[2]
        print(f'Third largest element in array is None')
        return None  # sorted_lst[len(sorted_lst)-1]
    except Exception as e:
        raise Exception('Error: ', e)


# Search an element in array(Understand how to traverse through the array and how to access the elements)
def search_element_in_Array(lst:[int], num:int):
    try:
        # s = num in lst
        ##### or ####
        s = list(filter(lambda x: x == num, lst))
        if len(s) > 0:
            print(f'{num} is exists in the list')
            return True
        print(f'{num} is not exists in the list')
        return False
    except Exception as e:
        raise Exception('Error: ', e)


## Find missing number in array
## ex: for 5 numbers from 1 to 5, find which number is missing inbetween
def missing_number_in_Array(lst):
    try:
        found = [i for i in range(1, len(lst) + 1) if i not in lst]
        if len(found) > 0:
            print(f'Missing number: {found}')
            return found
        return None
    except Exception as e:
        raise Exception('Error: ', e)


## Find repeating number in array
## ex: for 5 numbers from 1 to 5, find which number is repeating inbetween
def repeating_number_in_array(lst):
    try:
        # d=dict(enumerate(lst)) # [45,55,65] -> {0:45,1:55,2:65}
        # d = {i:0 for i in lst }
        d = dict.fromkeys(lst, 0)
        for i, j in d.items():
            d[i] = lst.count(i)
        print(d)
        return d
    except Exception as e:
        raise Exception('Error: ', e)


## Sort an array of 0s , 1s and 2s (You dont need to know any sorting algo, just using basics, once solved, definitely learn the optimal algo)
## {0, 1, 2, 0, 1, 2} -> {0,0,1,1,2,2}
def sort0s1s2s(lst):
    try:
        lo, mid, hi = 0, 0, len(lst) - 1
        while mid <= hi:
            if lst[mid] == 0:
                lst[lo], lst[mid] = lst[mid], lst[lo]
                mid += 1
                lo += 1
            elif lst[mid] == 1:
                mid += 1
            else:
                lst[mid], lst[hi] = lst[hi], lst[mid]
                hi -= 1
        print(lst)
        return lst
    except Exception as e:
        raise Exception('Error: ', e)


## Check if two arrays are equal or not
def check_equal_array_input(lst1, lst2):
    try:
        l1 = sorted(lst1)
        l2 = sorted(lst2)
        if l1 == l2:
            print(f'Elements are same')
            return True
        print(f'Elements are not same')
        return False
    except Exception as e:
        raise Exception('Error: ', e)


## Rotate the array by 1
def rotate_array(lst:[int]):
    try:
        n = len(lst)
        last_ele = lst[n-1]
        for i in range(n-1, 0, -1):
            lst[i] = lst[i-1]
        lst[0] = last_ele
        print(lst)
        return lst
    except Exception as e:
        raise Exception('Error: ', e)

## Rotate the array by k
# [1,2,3,4,5,6] , rotate 2 times. result => [5,6,1,2,3,4]
# step 1: [6,5,4,3,2,1]
# step 2: [5,6] + [1,2,3,4]
# step 3 : [5,6,1,2,3,4]
def left_rotation(nums, k):
    try:
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        return nums
    except Exception as e:
        raise Exception('Error: ', e)

## Array subset of another array
def subset_array(lst1, lst2):
    try:
        ss = list(map(lambda a: a in lst1, lst2))
        if False in ss:
            print(f'{lst2} is not a subset of {lst1}')
            return False
        print(f'{lst2} is a subset of {lst1}')
        return True
    except Exception as e:
        raise Exception('Error: ',e)

## Count frequency of elements in array(Solve efficiently, try applying what you learnt about map)
def frequency_of_element(lst,p):
    try:
        p = int(p)
        if p > len(lst):
            print(f'P={p}, but there are no {p} Index present so can\'t count the value.')
            return
        freq = list(map(lambda a: lst.count(a),range(1,p+1)))
        dict_freq = dict(enumerate(freq,start=1))
        print(dict_freq)
        return dict_freq
    except Exception as e:
        raise Exception('Error: ',e)



if __name__ == '__main__':
    n = int(input('Enter number of elements: '))
    lst = []
    for i in range(n):
        l = int(input(f'Enter number {i + 1} : '))
        lst.append(l)

    ## Find the maximum and minimum element in array(After solving the search , you can solve all probs in this basics by yourself)
    # max_min_array(lst)

    ## Find third largest element in array
    # third_largest(lst)

    ## Search an element in array(Understand how to traverse through the array and how to access the elements)
    # search = int(input('Enter an element to search: '))
    # search_element_in_Array(lst,search)

    ## Find missing number in array
    # missing_number_in_Array(lst)

    ## Find repeating number in array
    # repeating_number_in_array(lst)

    ## Sort an array of 0s , 1s and 2s (You dont need to know any sorting algo, just using basics, once solved, definitely learn the optimal algo)
    # sort0s1s2s(lst)

    ## Check if two arrays are equal or not
    # n1 = int(input('Enter number of elements: '))
    # lst1 = []
    # for i in range(n1):
    #     l = int(input(f'Enter number {i + 1} : '))
    #     lst1.append(l)
    # check_equal_array_input(lst, lst1)

    ## Rotate the array by 1
    # rotate_array(lst)

    ## Rotate the array by k
    # k = int(input('Enter rotate by: '))
    # left_rotation(lst,k)

    ## Array subset of another array
    # n1 = int(input('Enter number of elements: '))
    # lst1 = []
    # for i in range(n1):
    #     l = int(input(f'Enter number {i + 1} : '))
    #     lst1.append(l)
    # subset_array(lst,lst1)

    p = int(input('1 to P where elements can be repeated. Enter p: '))
    frequency_of_element(lst,p)