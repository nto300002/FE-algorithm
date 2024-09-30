def postfixtoinfix(exp):
    stack = []  # スタックをリストで初期化
    for i in range(len(exp)):  # リストの長さに従ってループ
        print(i)
        if isoperand(exp[i]):  # もしオペランドであれば
            stack.append(exp[i])  # スタックに追加
            print("isoperand == true:",stack)
        else:  # もし演算子であれば
            op1 = stack.pop()  # スタックからオペランドを取り出す
            op2 = stack.pop()
            # 括弧付きで演算子を中置記法に変換してスタックに戻す
            stack.append(f"({op2}{exp[i]}{op1})")
            print("isoperand == false:",stack)
            print(stack[0])
    
    # 最終結果を返す
    return stack[-1]

def isoperand(x):
    # オペランドかどうかを判断。演算子でなければオペランド。
    return x not in ["+", "-", "*", "/"]

# テスト
expression = "ab+c*"
result = postfixtoinfix(expression)
print("Postfix expression:", expression)
print("Infix expression:", result)
