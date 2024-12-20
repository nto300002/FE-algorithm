def runlength(a, m, b):
    c = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # 数字を表す文字列のリスト

    i = 0  # Pythonではインデックスが0から始まる
    j = 0  # b のインデックスを追跡する

    while i < m:  # i < m が正しい比較
        b.append(a[i])  # まず現在の文字をbに追加
        n = 1  # 現在の文字が連続しているかどうかのカウンター
        k = i + 1  # 次の文字のインデックス
        #print(b)

        while k < m and a[k] == a[i]:  # 次の文字が現在の文字と同じであればループ
            n += 1
            k += 1
            print("カウンター:",k)
        
        if n >= 3:  # もし3文字以上の連続があれば
            b.append(c[n-1])  # 連続した数をbに追加（cリストから）
            print("3文字以上:",c[n-1])
        elif n == 2:  # 2文字連続の場合
            b.append(a[i+1])  # そのまま次の文字を追加
            print("次の文字:",a[i+1])
        
        i = k  # 次の異なる文字に移動
        print("次の異なる文字に移動:",i)
        print("結果:",b)

runlength(['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'a'], 10, [])