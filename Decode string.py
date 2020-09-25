'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
'''


def decode_string(s):
    result = ''
    index = 0
    char_stack = []
    number_stack = []

    while index < len(s):
        if s[index].isdigit():
            number = 0
            while s[index].isdigit():
                number = number * 10 + int(s[index])
                index += 1
            number_stack.append(number)

        elif s[index].isalpha():
            result += s[index]
            index += 1

        elif s[index] == '[':
            char_stack.append(result)
            result = ""
            index += 1

        else:
            number = number_stack.pop()
            decode = char_stack.pop()
            temp = ""
            while number > 0:
                temp += result
                number -= 1
            result = decode + temp
            index += 1
    return result


if __name__ == '__main__':
    s = '3[a2[bc]]'
    print(decode_string(s))
