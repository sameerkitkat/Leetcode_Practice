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
