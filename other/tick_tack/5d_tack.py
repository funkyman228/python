# Constants for the dimensions of the game board
ROWS = 3
COLUMNS = 3
DEPTH = 3
WIDTH = 3
HEIGHT = 3

# Constants for the players
X = "X"
O = "O"

# The game board is represented as a list of lists of lists of lists of lists
board = []
for x in range(ROWS):
  column = []
  for y in range(COLUMNS):
    row = []
    for z in range(DEPTH):
      depth = []
      for w in range(WIDTH):
        width = []
        for h in range(HEIGHT):
          width.append(None)
        depth.append(width)
      row.append(depth)
    column.append(row)
  board.append(column)

# Print the game board
def print_board():
  for x in range(ROWS):
    for y in range(COLUMNS):
      for z in range(DEPTH):
        for w in range(WIDTH):
          for h in range(HEIGHT):
            if board[x][y][z][w][h] is None:
              print(" ", end="")
            else:
              print(board[x][y][z][w][h], end="")
            if h < HEIGHT - 1:
              print("|", end="")
          print()
        if w < WIDTH - 1:
          print("-+-+-")
        else:
          print()
      if z < DEPTH - 1:
        print("-+-+-+-")
      else:
        print()
    if y < COLUMNS - 1:
      print("-+-+-+--")
    else:
      print()

# Check if a player has won
def check_win(player):
  # Check rows
  for x in range(ROWS):
    for y in range(COLUMNS):
      for z in range(DEPTH):
        for w in range(WIDTH):
          if board[x][y][z][w] == [player, player, player, player, player]:
            return True
  
  # Check columns
  for y in range(COLUMNS):
    for z in range(DEPTH):
      for w in range(WIDTH):
        for h in range(HEIGHT):
          if board[0][y][z][w][h] == player and board[1][y][z][w][h] == player and board[2][y][z][w][h] == player:
            return True
  
  # Check depth
  for x in range(ROWS):
    for z in range(DEPTH):
      for w in range(WIDTH):
        for h in range(HEIGHT):
          if board[x][0][z][w][h] == player and board[x][1][z][w][h] == player and board[x][2][z][w][h] == player:
            return True
  
  # Check width
  for x in range(ROWS):
    for y in range(COLUMNS):
      for w in range(WIDTH):
        for h in range(HEIGHT):
          if board[x][y][0][w][h] == player and board[x][y][1][w][h] == player and board[x][y][2][w][h] == player:
            return True
  
  # Check height
  for x in range(ROWS):
    for y in range(COLUMNS):
      for z in range(DEPTH):
        for h in range(HEIGHT):
          if board[x][y][z][0][h] == player and board[x][y][z][1][h] == player and board[x][y][z][2][h] == player:
            return True
  
  # Check diagonals
  if board[0][0][0][0][0] == player and board[1][1][1][1][1] == player and board[2][2][2][2][2] == player:
    return True
  if board[0][2][0][0][0] == player and board[1][1][1][1][1] == player and board[2][0][2][2][2] == player:
    return True
  if board[0][0][2][0][0] == player and board[1][1][1][1][1] == player and board[2][2][0][2][2] == player:
    return True
  if board[0][2][2][0][0] == player and board[1][1][1][1][1] == player and board[2][0][0][2][2] == player:
    return True
  if board[0][0][0][2][0] == player and board[1][1][1][1][1] == player and board[2][2][2][0][2] == player:
    return True
  if board[0][2][0][2][0] == player and board[1][1][1][1][1] == player and board[2][0][2][0][2] == player:
    return True
  if board[0][0][2][2][0] == player and board[1][1][1][1][1] == player and board[2][2][0][0][2] == player:
    return True
  if board[0][2][2][2][0] == player and board[1][1][1][1][1] == player and board[2][0][0][0][2] == player:
    return True
  if board[0][0][0][0][2] == player and board[1][1][1][1][1] == player and board[2][2][2][2][0] == player:
    return True
  if board[0][2][0][0][2] == player and board[1][1][1][1][1] == player and board[2][0][2][2][0] == player:
    return True
  if board[0][0][2][0][2] == player and board[1][1][1][1][1] == player and board[2][2][0][2][0] == player:
    return True
  if board[0][2][2][0][2] == player and board[1][1][1][1][1] == player and board[2][0][0][2][0] == player:
    return True
  if board[0][0][0][2][2] == player and board[1][1][1][1][1] == player and board[2][2][2][0][0] == player:
    return True
  if board[0][2][0][2][2] == player and board[1][1][1][1][1] == player and board[2][0][2][0][0] == player:
    return True
  if board[0][0][2][2][2] == player and board[1][1][1][1][1] == player and board[2][2][0][0][0] == player:
    return True
  if board[0][2][2][2][2] == player and board[1][1][1][1][1] == player and board[2][0][0][0][0] == player:
    return True
  
  return False

# Main game loop
current_player = X
while True:
  # Print the game board
  print_board()
  
  # Get the player's move
  print("Player " + current_player + ", enter your move (x y z w h): ")
  x, y, z, w, h = map(int, input().split())
  
  # Make the move
  if board[x][y][z][w][h] is None:
    board[x][y][z][w][h] = current_player
    
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
