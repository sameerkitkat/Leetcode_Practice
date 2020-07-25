'''
In an alien language, surprisingly they also use english
lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase
letters.

Given a sequence of words written in the alien language,
and the order of the alphabet, return true if and only if the
given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"],
order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language,
then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"],
order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language,
then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"],
order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match,
and the second string is shorter (in size.)
According to lexicographical rules "apple" > "app",
because 'l' > '∅', where '∅' is defined as the blank character
which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''

charMap = [0] * 26
def verifyingAlienDictionary(words, order):
    for i in range(len(order)):
        charMap[ord(order[i]) - ord('a')] = i
    print(charMap)

    for i in range(0, len(words) - 1):
        if compare(words[i], words[i+1]) > 0:
            return False
    return True


def compare(word1, word2):
    i = j = val = 0
    while word1 and word2 and val == 0:
        val = charMap[ord(word1[i])- ord('a')] - charMap[ord(word2[j])- ord('a')]
        i += 1
        j += 1
    if val is 0:
        return len(word1) - len(word2)
    else:
        return val


if __name__ == '__main__':
    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    print(verifyingAlienDictionary(words,order))
