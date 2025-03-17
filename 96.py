def is_safe(num,row,col,board):
        for i in range(9):
            if num == board[row][i] or num == board[i][col]:
                return False
        x,y=(row//3)*3,(col//3)*3
        for i in range(x,x+3):
            for j in range(y,y+3):
                if board[i][j]==num:
                    return False
        return True
      
def helper(row,col,board):
        if row==9:
            return True
        nrow,ncol = row,col+1
        if col == 8:
            nrow+=1
            ncol = 0
        if board[row][col]!='.':
            if helper(nrow,ncol,board):
                return True
        else:
            for i in range(1,10):
                if is_safe(str(i),row,col,board):
                    board[row][col] = str(i)
                    if helper(nrow,ncol,board):
                        return True
                    else:
                        board[row][col]='.'

        return False

with open("96_sudoku.txt","r") as f:
   text = f.readlines()
   
result = 0
for i in range(0,50):
   raw_board = [row for row in text[i*10+1:i*10+10]]
   cleaned_board = [[] for i in range(9)]
   for i in range(9):
      for char in raw_board[i]:
         if char=='0':
            cleaned_board[i].append('.')
         else:
            cleaned_board[i].append(char)
   helper(0,0,cleaned_board)
   number = ''.join(cleaned_board[0][:3])
   result+=int(number)
print(result)
         
            
      
