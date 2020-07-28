'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer range:
[−231,  231 − 1]. 
For the purpose of this problem, assume that your
function returns 0 when the reversed integer overflows.
'''


def reverseInteger(n):
    if n < 0:
        return -1 * reverseUtil(abs(n))
    else:
        return reverseUtil(n)


def reverseUtil(n):
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n = n // 10
     if rev > pow(2,31) or rev < -pow(2,31):
        return 0
    else:
        return rev


if __name__ == '__main__':
    n = -123
    print(reverseInteger(n))
