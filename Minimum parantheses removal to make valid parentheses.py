'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses
( '(' or ')', in any positions ) so that the resulting
parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B),
where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)"
would also be accepted.

Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"


Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
'''


def MinimumParanthesisRemovalToMakeValid(s):
    indexes_to_remove = set()
    stack = []
    for i, c in enumerate(s):
        if c not in "()":
            continue
        if c == "(":
            stack.append(i)
        elif not stack:
            indexes_to_remove.add(i)
        else:
            stack.pop()
    print(indexes_to_remove)
    while stack:
        indexes_to_remove.add(stack.pop())
    print(indexes_to_remove)
    string_builder = ""
    for i, c in enumerate(s):
        if i not in indexes_to_remove:
            string_builder += c
    return string_builder


if __name__ == '__main__':
    s = "lee(t(c)o)d))e)"
    print(MinimumParanthesisRemovalToMakeValid(s))
