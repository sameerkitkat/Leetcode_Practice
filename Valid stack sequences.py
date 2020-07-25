def validStackSequence(pushed, popped):
    stack = []
    j = 0
    for i in pushed:
        stack.append(i)
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return len(popped) == j


if __name__ == '__main__':
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    print(validStackSequence(pushed,popped))
