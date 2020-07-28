'''
Given two non-negative integers num1 and num2 represented as
string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the
inputs to integer directly.
'''


def addStrings(s1, s2):
    carry = 0
    result = ''
    i, j = len(s1) - 1, len(s2) - 1
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += (ord(s1[i]) - ord('0'))
            i -= 1
        if j >= 0:
            carry += (ord(s2[j]) - ord('0'))
            j -= 1
        result += str(carry % 10)
        carry //= 10
    return result[::-1]


if __name__ == '__main__':
    s1 = "789"
    s2 = "456"
    print(addStrings(s1, s2))
