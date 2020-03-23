import math
import numpy

def printBoard(board):
  for i in range(0,5):
    for j in range(0,5):
      if i==1 or i==3:
        print('-', end='')
        continue
      if j==1 or j==3:
        print('|', end='')
        continue
      print(board[math.floor(i/2)][math.floor(j/2)], end="")
    print('')

def isOver(b):
  for i in range(0,3):
    if b[i][0]==b[i][1]==b[i][2]!=' ': return True
    if b[0][i]==b[1][i]==b[2][i]!=' ': return True
  if b[0,0]==b[1,1]==b[2,2]!=' ': return True
  if b[0,2]==b[1,1]==b[2,0]!=' ': return True
  return False


print("Welcome to The Python 3 Tic Tac Toe Game!!!")

p1Sign = input("Player 1 select your sign (X/0)\n").upper()

while p1Sign!='X' and p1Sign!='O':
  p1Sign = input("invalid input. Please enter 'X' or 'O'\n").upper()

p2Sign = "O" if p1Sign=="X" else "X"
playerSign = [p1Sign,p2Sign]
print(f"Player 1 is {p1Sign}")
print(f"Player 2 is {p2Sign}\n")

reference = []
for i in range(0,3):
  reference.append([])
  for j in range(0,3):
    reference[i].append(i*3+j)



board = numpy.full( (3,3),' ')
whosTurn="Player1"
sign=p1Sign

while not isOver(board):
  print("Reference board:")
  printBoard(reference)
  pos = input(f"{whosTurn}'s turn:\n")

  while not pos.isdigit() or int(pos)<0 or int(pos)>8 or board[math.floor(int(pos)/3)][int(pos)%3]!=" ":
    if board[math.floor(int(pos)/3)][int(pos)%3]!=" ":
      pos=input("invalid input. position is already filled. try again\n")
    else: 
      pos = input("Invalid input. Please enter an integer 0-8\n")

  pos=int(pos)

  print(f"{whosTurn} selected position: {pos}")
  board[math.floor(pos/3)][pos%3]=sign
  printBoard(board)

  whosTurn = "Player2" if whosTurn=="Player1" else "Player1"
  sign = p2Sign if sign==p1Sign else p1Sign