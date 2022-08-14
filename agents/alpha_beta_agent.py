from numpy.random import randint
class Alpha_Beta_Agent(object):
    def __init__(self,order):
        self.order = order

    def put_disc(self,choice, game_board):
        if choice<0 or choice>6:
            return -1
        if game_board[choice][0] != 0:
            return -1
        i = 0
        while i<6 and game_board[choice][i]==0:
            i=i+1
        return i-1

    def score_func(self, game_board, order, x, y):
        mid_score = 0
        if order == 0:
            return (False,0)
        game_board
        if x==3:
            mid_score+=7
        elif x==2 or x==4:
            mid_score+=3
        elif x==1 or x==5:
            mid_score+=1
        disc = game_board[x][y]

        # has_won down
        count = 0
        empties = 0
        i = y
        
        while i<6 and game_board[x][i]==disc:
            count+=1
            i+=1
        if i<6 and game_board[x][i]==0:
            empties+=1
        i = y-1
        
        while i>=0 and game_board[x][i]==disc:
            count+=1
            i-=1
        if i>=0 and game_board[x][i]==disc:
            empties+=1
        if count>=4:
            return (True,100000000000)
        elif count == 3 and empties == 2:
            # pravilo
            mid_score += 100
        elif count == 3 and empties == 1:
            # pravilo
            mid_score += 33
        elif count == 2 and empties == 1:
            # pravilo
            mid_score += 5
      

        # has_won sideways
        i = x
        count = 0
        empties = 0
        while i<7 and game_board[i][y]==disc:
            count+=1
            i+=1
        if i<7 and game_board[i][y]==0:
            empties+=1
        i=x-1
        while i>=0 and game_board[i][y]==disc:
            count+=1
            i-=1
        if i>=0 and game_board[i][y]==0:
            empties+=1

        if count>=4:
            return (True,100000000000)
        elif count == 3 and empties == 2:
            # pravilo
            mid_score += 100
        elif count == 3 and empties == 1:
            # pravilo
            mid_score += 33
        elif count == 2 and empties == 1:
            # pravilo
            mid_score += 5

        # has_won up-left to down-right
        i = x
        i2 = y
        count = 0
        empties = 0
        while i<7 and i2>=0 and game_board[i][i2]==disc:
            count+=1
            i+=1
            i2-=1
        if i<7 and i2>=0 and game_board[i][i2]==0:
            empties+=1
        i=x-1
        i2=y+1
        while i>=0 and i2<6 and game_board[i][i2]==disc:
            count+=1
            i-=1
            i2+=1
        if i>=0 and i2<6 and game_board[i][i2]==0:
            empties+=1

        if count>=4:
            return (True,100000000000)
        elif count == 3 and empties == 2:
            # pravilo
            mid_score += 100
        elif count == 3 and empties == 1:
            # pravilo
            mid_score += 33
        elif count == 2 and empties == 1:
            # pravilo
            mid_score += 5
        # has_won down-left to up-right
        i = x
        i2 = y
        count = 0
        empties = 0
        while i<7 and i2<6 and game_board[i][i2]==disc:
            count+=1
            i+=1
            i2+=1
        if i<7 and i2<6 and game_board[i][i2]==0:
            empties+=1
        i=x-1
        i2=y-1
        while i>=0 and i2>=0 and game_board[i][i2]==disc:
            count+=1
            i-=1
            i2-=1
        if i>=0 and i2>=0 and game_board[i][i2]==0:
            empties+=1

        if count>=4:
            return (True,100000000000)
        elif count == 3 and empties == 2:
            # pravilo
            mid_score += 100
        elif count == 3 and empties == 1:
            # pravilo
            mid_score += 33
        elif count == 2 and empties == 1:
            # pravilo
            mid_score += 5
        
        return (False,mid_score)
        
    def heuristic(self,game_board,order):
        # Heuristic function
        score = 0
        x = 0
        for column in game_board:
            y = 0
            for row in column:
                is_win, mid_score = self.score_func(game_board,game_board[x][y],x,y)
                if is_win:
                    if game_board[x][y]==order:
                        return mid_score
                    elif game_board[x][y]==order*-1:
                        return mid_score*-1

                if game_board[x][y]==order:
                    score+=mid_score
                elif game_board[x][y]==order*-1:
                    score-=mid_score
                    
                
                
                y+=1
            x+=1
        return score
    def evaluate(self, game_board, x,y, order, depth, turn, minmax, alpha, beta):
        is_win, score_ret = self.score_func(game_board,order*-1,x,y)
        if is_win:
            return score_ret*minmax*-1
        if depth == self.max_depth:
            return self.heuristic(game_board,order)
        if turn == 42:
            return 0
        xi=0
        best_score = -10000000000000000*minmax
        best_choice = -1
        for column in game_board:
            if column[0] == 0:
                yi = self.put_disc(xi,game_board)
                game_board[xi][yi] = order
                score = self.evaluate(game_board, xi, yi,order*-1, depth+1, turn+1, minmax*-1,alpha,beta)
                game_board[xi][yi] = 0
                # print(a+" CHOICE %d with score %d, %d"%(xi,score,minmax))
                if (score>best_score and minmax ==1) or (score<best_score and minmax ==-1):
                    best_score = score
                    best_choice = xi
                if minmax==1:
                    alpha = max(alpha,score)
                    if beta<alpha:
                        
                        # print("PRUNE %d <=%d : ret %d"%(beta,alpha,best_score))
                        return best_score
                elif minmax==-1:
                    beta = min(beta,score)
                    if beta<alpha:
                        # print("PRUNE %d <=%d : ret %d"%(beta,alpha,best_score))
                        return best_score
                
                
            xi+=1
        return best_score

    def move(self, game_board, turn):
        valid = []
        xi=0
        max_score = -10000000000000000
        alpha = -1000000000000000
                
        beta = 1000000000000000
        
        best_choice = -1
        for column in game_board:
            if column[0] == 0:
                yi = self.put_disc(xi,game_board)
                game_board[xi][yi] = self.order
                score = self.evaluate(game_board, xi, yi,self.order*-1, 1, turn, -1, alpha,beta)
                print("CHOICE %d with score %d"%(xi,score))
                alpha = max(alpha, score)
                if score>max_score:
                    valid = []
                    max_score = score
                    valid.append(xi)
                elif score == max_score:
                    valid.append(xi)
                game_board[xi][yi] = 0
            xi+=1
        choice = valid[randint(len(valid),size=1)[0]]
        print("PICKED %d WITH SCORE %d"%(choice,max_score))
        
        # time.sleep(10)
        return choice

    def set_max_depth(self, max_depth):
        self.max_depth = max_depth

    def introduce(self):
        return "SMART AGENT"