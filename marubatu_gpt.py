def get_player_names():
    """プレイヤーの名前を入力する関数"""
    player1 = input("プレイヤー1の名前を入力してください（X）: ")
    player2 = input("プレイヤー2の名前を入力してください（O）: ")
    return player1, player2

def create_board():
    """3x3の空のボードを作成する関数"""
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    """現在のボードの状態を表示する関数"""
    print("  0   1   2")
    for idx, row in enumerate(board):
        print(f"{idx} {row[0]} | {row[1]} | {row[2]}")
        if idx < 2:
            print("  --+---+--")
    print()

def check_winner(board, mark):
    """指定されたマークが勝者かどうかをチェックする関数"""
    # 行のチェック
    for row in board:
        if all(cell == mark for cell in row):
            return True
    
    # 列のチェック
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True
    
    # 斜めのチェック
    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2 - i] == mark for i in range(3)):
        return True
    
    return False

def is_draw(board):
    """ボードが引き分けかどうかをチェックする関数"""
    for row in board:
        if " " in row:
            return False
    return True

def get_move(player):
    """プレイヤーからの有効な移動を取得する関数"""
    while True:
        try:
            move = input(f"プレイヤー{player}のターンです。行と列をスペースで区切って入力してください（例: 0 1）: ")
            row, col = map(int, move.strip().split())
            if row not in range(3) or col not in range(3):
                print("行と列は0, 1, 2のいずれかで入力してください。")
                continue
            return row, col
        except ValueError:
            print("無効な入力です。数字をスペースで区切って入力してください。")

def play_game():
    """マルバツゲームを実行する関数（プレイヤー名対応版）"""
    board = create_board()
    player1, player2 = get_player_names()
    current_player = "X"  # プレイヤー1が"X"
    player_map = {"X": player1, "O": player2}
    
    while True:
        print_board(board)
        row, col = get_move(current_player)
        
        if board[row][col] != " ":
            print("その位置はすでに埋まっています。別の位置を選んでください。")
            continue
        
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"{player_map[current_player]}（プレイヤー{current_player}）の勝利です！")
            break
        
        if is_draw(board):
            print_board(board)
            print("引き分けです！")
            break
        
        # プレイヤーを交代
        current_player = "O" if current_player == "X" else "X"
