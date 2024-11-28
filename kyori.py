def levenshtein_distance_optimized(S, T):
    m = len(S)
    n = len(T)
    
    if m < n:
        # 文字列の長さが異なる場合、短い方を基準にする
        return levenshtein_distance_optimized(T, S)
    
    previous_row = list(range(n + 1))
    current_row = [0] * (n + 1)
    print(F"previous_row:{previous_row}")
    print(F"current_row:{current_row}")
    
    for i in range(1, m + 1):
        current_row[0] = i
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                cost = 0
            else:
                cost = 1
            print(F"S:{S} T:{T}")
            print(F"S[i - 1]:{S[i - 1]} T[j - 1]:{T[j - 1]} cost:{cost}")
            #print(F"current_row_for_j:{current_row}")
            current_row[j] = min(
                previous_row[j] + 1,      # 削除
                current_row[j - 1] + 1,   # 挿入
                previous_row[j - 1] + cost  # 置換
            )
            print(F"操作 pre{previous_row} curr{current_row}")
        # 行の更新
        previous_row, current_row = current_row, previous_row
    
    return previous_row[n]

# 入力の受け取り
if __name__ == "__main__":
    S = "ajkskkjajkkk"
    T = "iaailkdl"
    
    distance = levenshtein_distance_optimized(S, T)
    
    print(f"SをTに変換するための最小操作回数（編集距離）は: {distance}")
