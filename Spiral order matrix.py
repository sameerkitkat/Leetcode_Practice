'''
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


def spiralOrderMatrix(matrix):
    top = left = 0
    bottom , right = len(matrix)-1, len(matrix[0])-1
    size = len(matrix) * len(matrix[0])
    ans = []
    while len(ans) < size:
        for i in range(left, right + 1):
            if len(ans) < size:
                ans.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            if len(ans) < size:
                ans.append(matrix[i][right])
        right -= 1

        for i in range(right, left - 1, -1):
            if len(ans) < size:
                ans.append(matrix[bottom][i])
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            if len(ans) < size:
                ans.append(matrix[i][left])
        left += 1
    return ans


if __name__ == '__main__':
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    print(spiralOrderMatrix(matrix))
