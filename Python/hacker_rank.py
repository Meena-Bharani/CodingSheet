#### https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
def minion_game(string):
    # string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
    import string as st
    vowels = 'AEIOU'
    consonants = ''.join([letter for letter in st.ascii_uppercase if letter not in vowels])
    kevin_score = 0
    stuart_score = 0

    for i, j in enumerate(string):
        if j in vowels:
            kevin_score += len(string[i:])
        elif j in consonants:
            stuart_score += len(string[i:])
    if kevin_score > stuart_score:
        print('Kevin', kevin_score)
    elif stuart_score > kevin_score:
        print('Stuart', stuart_score)
    elif kevin_score == stuart_score:
        print('Draw')

###   https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
def merge_the_tools(string, k):
    # your code goes here
    l = len(string)
    # lst = [''.join(set(string[i:i+k])) for i in range(0,l,k)]
    lst = [string[i:i + k] for i in range(0, l, k)]
    for i in lst:
        seen = set()
        seen_add = seen.add
        s = [x for x in i if not (x in seen or seen_add(x))]
        print(''.join(s))

## https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
# You gain  unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B. The element 7 in set B does not exist in the array so it is not included in the calculation.
# Hence, the total happiness is 2-1=1.

def no_idea():
    n,m = list(map(int,input().split()))
    interest = [s for s in input().split()]
    A = {s for s in input().split()}
    B = {s for s in input().split()}
    happiness = sum([1 if i in A else -1 if i in B else 0 for i in interest])
    print(happiness)

## https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
# triangle, 90 degree  at B.Therefore, angle ABC=90 degree.
# Point M is the midpoint of hypotenuse AC.
# You are given the lengths AB and BC.
# Your task is to find angle MBC (angle , as shown in the figure) in degrees.

from math import sqrt, acos, degrees
def find_angle():
    AB = int(input())
    BC = int(input())
    h = sqrt(AB**2 + BC**2)
    theta = round(degrees(acos(BC/h)))
    print(theta,chr(176),sep='')


###  https://www.hackerrank.com/challenges/triangle-quest-2/problem?isFullScreen=true
# # 1
# # 121
# # 12321
# # 1234321
# # 123454321
def triangle_quest_2():
    n=5
    for i in range(1,n+1):
        # z = [*[str(i) for i in range(1,i+1)],*[str(i) for i in range(i-1,0,-1)]]
        # print(''.join(z))
        z = ((10**i)//9)**2
        print(z)


def collections_defaultdict():
    from collections import defaultdict
    n, m = map(int, input().strip().split())
    d = defaultdict(list)
    [d[input()].append(i + 1) for i in range(n)]
    [print(*d.get(input(), -1)) for _ in range(m)]

    # n, m = list(map(int, input().strip().split()))
    # d = defaultdict(list)
    # for i in range(n):
    #     inp = input()
    #     if inp not in d.keys():
    #         d[inp] = []
    #     d[inp].append(i+1)
    # for i in range(m):
    #     inp = input()
    #     if inp in d.keys():
    #         print(' '.join(list(map(str,d[inp]))))
    #     else:
    #         print(-1)

# https://www.hackerrank.com/test/4nahpm20m33/questions/di1dm3kpigj
# Flipping matrix:
# Get max from Element1 => (R0,C0) (R0,C3) (R3,C0) (R3,C3)   119
# Get max from Element2 => (R0,C1) (R0,C2) (R3,C1) (R3,C2)   142
# Get max from Element3 => (R1,C0) (R1,C3) (R2,C0) (R2,C3)   56
# Get max from Element4 => (R1,C1) (R1,C2) (R2,C1) (R2,C2)   125
#
# Row   0  0  3  3      i   i  2n-i-1   2n-i-1
# Row   0  0  3  3
# Row   1  1  2  2
# Row   1  1  2  2
#
# Col   0  3  0  3      j  2n-j-1   j   2n-j-1
# Col   1  2  1  2
# Col   0  3  0  3
# Col   1  2  1  2

sum = 0
_max =0
for i in range(n):
    for j in range(n):
        max(matrix[i][j],

##############################################################
# if string is 'agelimit' pattern is '010'
#         age
#         [True, True, True]
#         1
#         gel
#         [False, False, False]
#         0
#         eli
#         [True, True, True]
#         1
#         lim
#         [False, False, False]
#         0
#         imi
#         [True, True, True]
#         1
#
        vw='aeiouy'
        s = 'codesignal'
        s = 'agelimit'
        p = 100
        p = '010'
        sp = str(p)
        n = (len(s) // len(sp)) * len(sp) - 1
        for i in range(n):
            ts = s[i:i + len(sp)]
        print(ts)
        # x = [lambda a,b: True if (a=='0' and b in vw) else (True if (a=='1' and b not in vw) else False) ,list(zip(sp,ts))]
        # x =list(map(True for a,b in list(zip(sp,ts)) if (a=='0' and b in vw) else (True if a=='1' and b not in vw else False)))
        # x = [(lambda x,y: x-y if x>y else y-x)(x,y) for x,y in zip(v1,v2)]
        x = [(lambda a, b: True if (a == '0' and b in vw) else (True if (a == '1' and b not in vw) else False))(a, b)
             for a, b in zip(sp, ts)]
        y = [(lambda a, b: 1 if (a == '0' and b in vw) else (1 if (a == '1' and b not in vw) else 0))(a, b) for a, b in
             zip(sp, ts)]
        print(x)
        print(int(sum(y) / len(sp)))



if __name__ == '__main__':
    s = input()
    minion_game(s) # input BANANA # output Stuart 12
    #######################
    AABCAAADA
    ## input s = 'AABCAAADA'      k = 3
    ##output AB CA AD
    string, k = input(), int(input())
    merge_the_tools(string, k)
    #######################
    #inputs
    # 3 2
    # 1 5 3
    # 3 1
    # 5 7
    # output
    #1
    no_idea()
    #######################
    #inout
    #10
    #10
    #output
    # 45 degree
    find_angle()
    #######################
    triangle_quest_2()
    #######################
    # sample input
    # STDIN   Function
    # -----   --------
    # 5 2     group A size n = 5, group B size m = 2
    # a       group A contains 'a', 'a', 'b', 'a', 'b'
    # a
    # b
    # a
    # b
    # a       group B contains 'a', 'b'
    # b
    # Sample Output
    # 1 2 4
    # 3 5
    collections_defaultdict()
    #######################
    #######################
    #######################
    #######################