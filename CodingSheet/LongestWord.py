''' Write a function that takes a sentance, and returns the longest word in the sentance
or if it has no even-length words, return '00'.
'''

def longest_even(text):
    longest = '00'
    for word in text.split():
        if len(word) % 2 ==0 and len(word) >= len(longest):
            longest = word
    return longest

strings = [
    'this is my apple' # 'this'
    ,'' #'00'
    ,'this is a longest sentence' #sentence
    ,'a bbb ccccc' # '00'
]

for string in strings:
    print(f"'{string}' -> '{longest_even(string)}'")