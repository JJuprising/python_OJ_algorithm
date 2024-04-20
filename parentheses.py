def generateParenthesis(n):
    result = []

    def backtrack(lst, left, right):
        print(lst)
        if len(lst) == 2 * n:
            result.append(''.join(lst))
            return  # 什么都不反回，仅作为递归的出口,即返回[]

        # 两个限制条件(if语句)顺序可以替换
        if left < n:
            # 探索当前位置放入左括号的所有组合
            lst.append('(')
            print(lst)
            # 核心回溯语句
            backtrack(lst, left + 1, right)
            # 将放入的左括号删除u，因为该位置也可能可以放入右括号
            # 我们删除后继续探索放入右括号的所有有效组合(下一个if语句)
            lst.pop()
            print(lst)

        # 同理
        if right < left:
            # 探索当前位置放入右括号的所有组合
            lst.append(')')
            print(lst)
            # 核心回溯语句
            backtrack(lst, left, right + 1)
            # 将放入的右括号删除，因为该位置也可能可以放入左括号
            # 我们删除后继续探索剩下的有效组合
            lst.pop()
            print(lst)


    backtrack([], 0, 0)
    return result

n = int(input())
valid_parentheses = generateParenthesis(n)
print("[{}]".format(", ".join(valid_parentheses)))