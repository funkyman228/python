# Constants for the dimensions of the game board
ROWS = 3
COLUMNS = 3
DEPTH = 3

# Constants for the players
X = "X"
O = "O"

# The game board is represented as a list of lists of lists
board = []
for x in range(ROWS):
  column = []
  for y in range(COLUMNS):
    row = []
    for z in range(DEPTH):
      row.append(None)
    column.append(row)
  board.append(column)

# Print the game board
def print_board():
  for x in range(ROWS):
    for y in range(COLUMNS):
      for z in range(DEPTH):
        if board[x][y][z] is None:
          print(" ", end="")
        else:
          print(board[x][y][z], end="")
        if z < DEPTH - 1:
          print("|", end="")
      print()
    if y < COLUMNS - 1:
      print("-+-+-")
    else:
      print()

# Check if a player has won
def check_win(player):
  # Check rows
  for x in range(ROWS):
    for y in range(COLUMNS):
      if board[x][y] == [player, player, player]:
        return True
  
  # Check columns
  for y in range(COLUMNS):
    for z in range(DEPTH):
      if board[0][y][z] == player and board[1][y][z] == player and board[2][y][z] == player:
        return True
  
  # Check depth
  for x in range(ROWS):
    for z in range(DEPTH):
      if board[x][0][z] == player and board[x][1][z] == player and board[x][2][z] == player:
        return True
  
  # Check diagonals
  if board[0][0][0] == player and board[1][1][1] == player and board[2][2][2] == player:
    return True
  if board[0][2][0] == player and board[1][1][1] == player and board[2][0][2] == player:
    return True
  if board[0][0][2] == player and board[1][1][1] == player and board[2][2][0] == player:
    return True
  if board[0][2][2] == player and board[1][1][1] == player and board[2][0][0] == player:
    return True
  
  return False

# Main game loop
current_player = X
while True:
  # Print the game board
  print_board()
  
  # Get the player's move
  print("Player " + current_player + ", enter your move (x y z): ")
  x, y, z = map(int, input().split())
  
  # Make the move
  if board[x][y][z] is None:
    board[x][y][z] = current_player
    
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
