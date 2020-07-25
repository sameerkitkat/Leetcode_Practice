'''
Given an array of integers and an integer k, you need to find
the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2


Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range
of the integer k is [-1e7, 1e7].
'''


def subarraysWithGivenSum(arr,k):
    arrSum = count = 0
    myDict = {0 : 1}
    for i in range(0, len(arr)):
        arrSum += arr[i]
        count += myDict.get(arrSum - k, 0)
        myDict[arrSum] = myDict.get(arrSum, 0) + 1
    return count


if __name__ == '__main__':
    arr = [1, 2, 3]
    k = 3
    print(subarraysWithGivenSum(arr,k))
