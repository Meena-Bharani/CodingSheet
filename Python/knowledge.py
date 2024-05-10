l = 'aabcabbcabcabc'
count =3 # split as a chars => abc abc abc abc
splitting = list(zip(*[iter(l)] * count))
print(set(splitting))


####################
## input ('AABCAAADA' ,3)

# output
# Split s into n/k = 9/3 = 3 equal parts of length k=3.
# Convert each  'ti' to 'ui' by removing any subsequent occurrences of non-distinct characters in 'ti':
#
# Print each 'ui' on a new line.
# 1. t0 = 'AAB' -> u0 = 'AB'
# 2. t1 = 'CAA' -> u1 = 'CA'
# 3. t2 = 'ADA' -> u2 = 'AD'

def merge_the_tools(string, k):
    l = len(string)
    lst = [string[i:i+k] for i in range(0,l,k)]
    for i in lst:
        seen = set()
        seen_add = seen.add
        s = [x for x in i if not(x in seen or seen_add(x))]
        print(''.join(s))

