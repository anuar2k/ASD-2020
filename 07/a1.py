def check(brackets):
    stack = [None] * (len(brackets) // 2)
    stackPtr = 0

    for bracket in brackets:
        if bracket == '(' or bracket == '[':
            if stackPtr < len(stack):
                stack[stackPtr] = bracket
                stackPtr += 1
            else:
                return False
        elif bracket == ')' or bracket == ']':
            stackPtr -= 1
            if stackPtr >= 0:
                if bracket == ')':
                    if stack[stackPtr] != '(':
                        return False
                else:
                    if stack[stackPtr] != '[':
                        return False
            else:
                return False

    return True

print(check("((asd))[asd][]ad([(asd)das])"))