'''
Given a string, find the length of the longest
substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring,
             "pwke" is a subsequence and not a substring.
'''




def longestSubstringWithoutRepeatingCharacters(s):
    mySet = set()
    ans = i = j = 0
    while i < len(s) and j < len(s):
        if s[j] not in mySet:
            mySet.add(s[j])
            j += 1
            ans = max(ans, j - i)
        else:
            mySet.remove(s[i])
            i += 1
    return ans


if __name__ == '__main__':
    s = "abcabcbb"
    print(longestSubstringWithoutRepeatingCharacters(s))
