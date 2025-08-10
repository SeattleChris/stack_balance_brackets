#!/bin/python3

import os

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

BRACKETS = {'(': ')', '[': ']', '{': '}'}

def response(is_matched: bool):
    return 'YES' if is_matched else 'NO'


def isBalanced(s):
    stack, needed = [], []
    for ea in s:
        if stack and needed:
            if needed[-1] == ea:
                stack.pop()
                needed.pop()
                continue
        if ea not in BRACKETS:  # unmatched closing bracket or invalid str
            return response(False)
        stack.append(ea)
        needed.append(BRACKETS[ea])
    return response(not stack)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + '\n')
    fptr.close()
