import numpy as np
import pandas as pd
rows = np.unique(np.random.randint(10000,size=1500))
df = pd.read_csv('c4_game_database.csv')
df= df.dropna()
for row in rows:
    
    
    arr=df.iloc[row].to_numpy().tolist()
    
    outcome=arr.pop()

    board = []
    while len(arr)>0:
        buf = arr[:7]
        
        board.append(buf)
        arr=arr[7:]
    board.reverse()

    out=[]
    x=0
    while x<7:
        y=0
        while y<6:
            out.append(board[y][x])
            y+=1
        x+=1
    out.append(outcome)
    output = ""
    for x in out:
        output+="%d,"%int(x)
    output = output[:-1]
    print(output)