#Proyetei Akanda

class CheckersGame () :
    
    #initializes board
    def __init__ (self) :
        self.coins = ('empty space','white checker','red checker','white king','red king')
        self.board =  [ [ 0, 2, 0, 2, 0, 2, 0, 2 ]
                      , [ 2, 0, 2, 0, 2, 0, 2, 0 ]
                      , [ 0, 2, 0, 2, 0, 2, 0, 2 ]
                      , [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                      , [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                      , [ 1, 0, 1, 0, 1, 0, 1, 0 ]
                      , [ 0, 1, 0, 1, 0, 1, 0, 1 ]
                      , [ 1, 0, 1, 0, 1, 0, 1, 0 ]
                      ]

        self.whoseMove = "white"
        self.isWon = 0
        
    #check winner 
    def checkWinner(self) :
        countw = 0
        countr = 0
        for i in self.board:
            for j in i:
                if j == 1 or j == 3:
                    countw += 1
                elif j == 2 or j == 4:
                    countr += 1
                else:
                    continue
        if countr == 0:
            self.isWon = 'white'
        elif countw == 0:
            self.isWon = 'red'
            
            
    def changeTurn(self) :
        if self.whoseMove == "white":
            self.whoseMove = "red"
        elif self.whoseMove == "red":
            self.whoseMove = "white"  
            
    #make move        
    def move(self, move) :
        pmove = self.parseMove(move)
        for i in range(len(pmove)-1):
            (y,x) = (pmove[i])
            (y2,x2) = (pmove[i+1])
            a = self.board[y][x]
            if self.coins[self.board[y][x]] == 'white checker' :
                if y2 == 0:
                    a = 3
            elif self.coins[self.board[y][x]] == 'red checker':
                if y2 == 7:
                    a = 4  
            if abs(y2-y) == 1 and abs(x2-x) == 1:
                self.board[y2][x2] = a
                self.board[y][x] = 0
                
            elif abs(y2-y) == 2 and abs(x2-x) == 2:
                (y1,x1) = (int((y+y2)/2), int((x+x2)/2))
                self.board[y2][x2] = a
                self.board[y][x] = 0
                self.board[y1][x1] = 0
        self.changeTurn()
        self.checkWinner()
        
        #checks if the move is valid
        def isValidMove(self, move) : 
            if self.isWon == 0:
                pmove = self.parseMove(move)
                (y,x) = pmove[0]
                pos = self.board[y][x]
                wmove = self.whoseMove         
                if self.coins[pos][:3] != self.whoseMove[:3]:
                    return False
                else:
                    for i in range(len(pmove)-1):
                        (y,x) = (pmove[i])
                        (y2,x2) = (pmove[i+1])
                        if (self.board[y2][x2] == 0 or ((y2,x2) in pmove)) and ((pos == 3) or (pos == 4)):  
                            
                            if abs(y2-y) == 1 and abs(x2-x) == 1:
                                continue
                            elif abs(y2-y) == 2 and abs(x2-x) == 2:
                                (y1,x1) = (int((y+y2)/2), int((x+x2)/2))
                                if (self.board[y1][x1] != 0) and (self.coins[self.board[y1][x1]][:3] !=  self.whoseMove[:3]):
                                    continue
                                else:
                                    return False
                            else:
                                return False
                        elif (self.board[y2][x2] == 0) and (pos == 1):
                            
                            if (y-y2 == 1) and (abs(x2-x) == 1):
                                continue
                            elif (y-y2 == 2) and abs(x2-x) == 2:
                                (y1,x1) = (int((y+y2)/2), int((x+x2)/2))
                                if (self.board[y1][x1] != 0) and (self.coins[self.board[y1][x1]][:3] !=  self.whoseMove[:3]):
                                    continue
                                else:
                                    return False
                            else:
                                return False
                        elif (self.board[y2][x2] == 0) and (pos == 2):
                            
                            if y2-y == 1 and abs(x2-x) == 1:
                                continue
                            elif (y2-y == 2) and (abs(x2-x) == 2):
                                (y1,x1) = (int((y+y2)/2), int((x+x2)/2))
                                if (self.board[y1][x1] != 0) and (self.coins[self.board[y1][x1]][:3] !=  self.whoseMove[:3]):
                                    continue
                                else:
                                    return False
                            else:
                                return False
                            
                        else:
                            return False
                    return True
            else:
                return False
    #draws out the checkers board  
    def __str__ (self) :
        out = "  0 1 2 3 4 5 6 7 \n  ╔═╤═╤═╤═╤═╤═╤═╤═╗\n"
        i = 0
        for row in self.board :
            out += f"{str(i)}║"
            j = 0
            for item in row :
                if item == 0:
                    out += "░" if (i + j) % 2 == 0 else " "
                elif item >= 1 and item <= 4:
                    out += ["○", "●", "♔", "♚"][item-1]
                out += "│"
                j += 1
            out = out[:-1]
            out += f"║{str(i)}\n ╟─┼─┼─┼─┼─┼─┼─┼─╢\n"
            i += 1
        out = out[:-18]
        out += "╚═╧═╧═╧═╧═╧═╧═╧═╝\n  0 1 2 3 4 5 6 7 \n"
        return out
      
     