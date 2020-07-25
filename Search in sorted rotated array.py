'''
Suppose an array sorted in ascending order is rotated at
some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array
return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of
O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


def searchInSortedRotatedArray(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] >= arr[start]:
            if target >= arr[start] and target < arr[mid]:
                end =  mid - 1
            else:
                start = mid + 1
        else:
            if target <= arr[end] and target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


if __name__ == '__main__':
    arr = [4,5,6,7,8,0,1,2,3]
    print(searchInSortedRotatedArray(arr,6))
