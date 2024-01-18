# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# 150. Evaluate Reverse Polish Notation
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                a, b =stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a, b =stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))
        return int(stack[0])

# https://leetcode.com/problems/isomorphic-strings/description/
# 205. Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Example 2
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
# Input: s = "paper", t = "title"
# Output: true

# hash1 = {f:b,    hash2 = {b:f,
#          o:a,             a:o,
#          o:r}             r:o}
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap1 , hashmap2 = {}, {}
        for char1, char2 in zip(s, t):
            if ((char1 in hashmap1 and hashmap1[char1] != char2) or (char2 in hashmap2 and hashmap2[char2] != char1)):
                return False
            hashmap1[char1] = char2
            hashmap2[char2] = char1
        return True

