'''
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal
to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements
of any prefix or suffix of the array (including the whole array)
fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose
of space complexity analysis.)
'''


def arrayProductExceptSelf(arr):
    n = len(arr)
    L, R, ans = [0] * n, [0] * n, [0] * n
    L[0] = 1
    for i in range(1, n):
        L[i] = arr[i - 1] * L[i - 1]
    R[n - 1] = 1
    for i in reversed(range(n - 1)):
        R[i] = arr[i + 1] * R[i + 1]
    for i in range(n):
        ans[i] = L[i] * R[i]
    return ans


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(arrayProductExceptSelf(arr))
