'''
This is asked in pubmatic

Remove all the duplicates from array

Example 1:

Input: arr = [1,1,1,1,2,2,2,1,1,3,1,1]
Output: [3]
Explanation:
Remove all 1s and 2s present at begining
then 1s after that and 1s after 3
'''


def removeConsecutiveDuplicates(arr):
    stack = []
    lastVisited = 0
    for i in range(len(arr)):
        if arr[i] not in stack and arr[i] != lastVisited:
            stack.append(arr[i])
            lastVisited = arr[i]
        elif len(stack) != 0:
            stack.pop()
    return stack


if __name__ == '__main__':
    arr = [1,1,1,1,2,2,2,1,1,3]
    print(removeConsecutiveDuplicates(arr))
