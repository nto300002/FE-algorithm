def replace_tab_with_spaces(a, m, b, l, n):
    # bを初期化（aの内容をベースに作るため、最初は空のリストとしておく）
    b = []
    nn = n
    
    # 'tab' を n 文字分の空白に置き換え
    for i in range(m):
        if a[i] == 'tab':
            for j in range(n):
                b.append(' ')# n 文字分の空白を追加
        else:
            b.append(a[i])  # それ以外はそのままコピー
    
    # b の長さを計算
    l = len(b)
    
    return b, l

# テストデータ
a = ['hello', 'tab', 'world', 'tab', '!']
m = len(a)
b = []  # 空の配列として初期化
l = 0   # 最初は0
n = 4   # 例えば、'tab' を4文字の空白に置き換えるとする

# 関数の実行
b, l = replace_tab_with_spaces(a, m, b, l, n)

# 結果を表示
print("置き換え後の配列:", b)
print("新しい配列の長さ:", l)

