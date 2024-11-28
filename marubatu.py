#〇×

class Player:
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col
    
    def info(self):
        print(F"{self.name}: row:{self.row} col:{self.col}")

def marubatu(name,n,m,field):

    #[0][1] 行列で指定
    if name == "one":
        field[n][m] = 1
    elif name == "two":
        field[n][m] = 2
    else:
        field[n][m] = 0
        
    for row in field:
        print(row)
    print("-------")
    
    player1_flag = 1
    player2_flag = 2
    
    p1_cnt = 0
    p2_cnt = 0
    for i in field:
        if field[i][0] == player1_flag:
            p1_cnt += 1
        elif field[i][0] == player2_flag:
            p2_cnt += 1
            
    p1_cnt = 0
    p2_cnt = 0           
    for i in field:   
        if field[0][i] == player1_flag:
            p1_cnt += 1
        elif field[0][i] == player2_flag:
            p2_cnt += 1
            
    p1_cnt = 0
    p2_cnt = 0            
    for i in field:         
        if field[i][i] == player1_flag:
            p1_cnt += 1
        elif field[i][i] == player2_flag:
            p2_cnt += 1
    
    if p1_cnt == 3:
        print("p1_win!")
    elif p2_cnt == 3:
        print("p2_win!")
        
        

marubatu_field = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]
player1_name = "one"
player2_name = "two"

player1 = Player(player1_name,1,1)
marubatu(player1.name,player1.row,player1.col,marubatu_field)

player2 = Player(player2_name,0,1)
marubatu(player2.name,player2.row,player2.col,marubatu_field)

player1 = Player(player1_name,0,2)
marubatu(player1.name,player1.row,player1.col,marubatu_field)

player2 = Player(player2_name,2,0)
marubatu(player2.name,player2.row,player2.col,marubatu_field)

player1 = Player(player1_name,0,2)
marubatu(player1.name,player1.row,player1.col,marubatu_field)

player2 = Player(player2_name,2,2)
marubatu(player2.name,player2.row,player2.col,marubatu_field)

player1 = Player(player1_name,1,0)
marubatu(player1.name,player1.row,player1.col,marubatu_field)

player1 = Player(player1_name,1,2)
marubatu(player1.name,player1.row,player1.col,marubatu_field)