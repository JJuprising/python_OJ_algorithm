def PN(digits):
    digitMap = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    if digits =="":
        return[]
    if len(digits) == 1:
        return digitMap[digits]

    result = []
    def backtrace(index,alpha):
        if index == len(digits):
            result.append(alpha)
            return
        for i in digitMap[digits[index]]:
            backtrace(index+1,alpha+i)
    backtrace(0,"")
    return result

digits = str(input())
res=PN(digits)
output_list = [elem.strip("'") for elem in res]
# print(output_list)
output_str = ', '.join(output_list)
print('[' + output_str + ']')
