import string

def extracharcter(a, b):
    n = {char: 0 for char in string.ascii_lowercase}  # 辞書を使う
    print(n)

    for char in b:  # b の各文字に対して処理
        if char in n:  # もし辞書にその文字があれば
            n[char] += 1
            print('b:', n[char])
            print(n)
    
    for char in a:  # a の各文字に対して処理
        if char in n:  # もし辞書にその文字があれば
            n[char] -= 1
            print('a:', n[char])
            print(n)
    
    for char, count in n.items():  # 辞書内で0でない文字を探す
        if count != 0:
            print(char)
            break

# テストケース
extracharcter(["a", "a", "b", "c", "d", "a"], ["a", "a", "b", "c", "d", "a", "v"])