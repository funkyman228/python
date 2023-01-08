# Constants for the dimensions of the game board
ROWS = 3
COLUMNS = 3
DEPTH = 3
WIDTH = 3

# Constants for the players
X = "X"
O = "O"

# The game board is represented as a list of lists of lists of lists
board = []
for x in range(ROWS):
  column = []
  for y in range(COLUMNS):
    row = []
    for z in range(DEPTH):
      depth = []
      for w in range(WIDTH):
        depth.append(None)
      row.append(depth)
    column.append(row)
  board.append(column)

# Print the game board
def print_board():
  for x in range(ROWS):
    for y in range(COLUMNS):
      for z in range(DEPTH):
        for w in range(WIDTH):
          if board[x][y][z][w] is None:
            print(" ", end="")
          else:
            print(board[x][y][z][w], end="")
          if w < WIDTH - 1:
            print("|", end="")
        print()
      if z < DEPTH - 1:
        print("-+-+-")
      else:
        print()
    if y < COLUMNS - 1:
      print("-+-+-+-")
    else:
      print()

# Check if a player has won
def check_win(player):
  # Check rows
  for x in range(ROWS):
    for y in range(COLUMNS):
      for z in range(DEPTH):
        if board[x][y][z] == [player, player, player, player]:
          return True
  
  # Check columns
  for y in range(COLUMNS):
    for z in range(DEPTH):
      for w in range(WIDTH):
        if board[0][y][z][w] == player and board[1][y][z][w] == player and board[2][y][z][w] == player:
          return True
  
  # Check depth
  for x in range(ROWS):
    for z in range(DEPTH):
      for w in range(WIDTH):
        if board[x][0][z][w] == player and board[x][1][z][w] == player and board[x][2][z][w] == player:
          return True
  
  # Check width
  for x in range(ROWS):
    for y in range(COLUMNS):
      for w in range(WIDTH):
        if board[x][y][0][w] == player and board[x][y][1][w] == player and board[x][y][2][w] == player:
          return True
  
  # Check diagonals
  if board[0][0][0][0] == player and board[1][1][1][1] == player and board[2][2][2][2] == player:
    return True
  if board[0][2][0][0] == player and board[1][1][1][1] == player and board[2][0][2][2] == player:
    return True
  if board[0][0][2][0] == player and board[1][1][1][1] == player and board[2][2][0][2] == player:
    return True
  if board[0][2][2][0] == player and board[1][1][1][1] == player and board[2][0][0][2] == player:
    return True
  if board[0][0][0][2] == player and board[1][1][1][1] == player and board[2][2][2][0] == player:
    return True
  if board[0][2][0][2] == player and board[1][1][1][1] == player and board[2][0][2][0] == player:
    return True
  if board[0][0][2][2] == player and board[1][1][1][1] == player and board[2][2][0][0] == player:
    return True
  if board[0][2][2][2] == player and board[1][1][1][1] == player and board[2][0][0][0] == player:
    return True
  
  return False

# Main game loop
current_player = X
while True:
  # Print the game board
  print_board()
  
  # Get the player's move
  print("Player " + current_player + ", enter your move (x y z w): ")
  x, y, z, w = map(int, input().split())
  
  # Make the move
  if board[x][y][z][w] is None:
    board[x][y][z][w] = current_player
    
    # Check if the player has won
    if check_win(current_player):
      print("Player " + current_player + " has won!")
      break
    
    # Switch to the other player
    if current_player == X:
      current_player = O
    else:
      current_player = X
  else:
    print("That space is already occupied! Please try again.")
