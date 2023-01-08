import socket
import threading

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
      for z in range(DEPTH):
        if board[x][y][z] == player:
          if (z == DEPTH - 1 or (z < DEPTH - 1 and board[x][y][z+1] == player)):
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

# A class for handling communication with each client
class ClientHandler(threading.Thread):
  def __init__(self, client_socket, client_address):
    threading.Thread.__init__(self)
    self.client_socket = client_socket
    self.client_address = client_address
  
  def run(self):
    # Send the current state of the game board to the client
    self.client_socket.sendall(str(board).encode())
    
    # The main game loop
    current_player = X
    while True:
      # Receive a move from the client
      data = self.client_socket.recv(1024).decode()
      
      # If the client has closed the connection, exit the game loop
      if not data:
        break
      
      # Parse the move from the client
      x, y, z = map(int, data.split())
      
      # Make the move and update the game board
      if board[x][y][z] is None:
        board[x][y][z] = current_player
        
        # Check if the player has won
        if check_win(current_player):
          self.client_socket.sendall(("You have won!").encode())
          break
        
        # Send the updated game board to all clients
        for client in clients:
          client.client_socket.sendall(str(board).encode())
        
        # Switch to the other player
        if current_player == X:
          current_player = O
        else:
          current_player = X
      else:
        self.client_socket.sendall(("That space is already occupied! Please try again.").encode())
    
    # Remove the client from the list of clients
    clients.remove(self)

# The list of connected clients
clients = []

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an IP address and port
server_socket.bind(("0.0.0.0", 8000))

# Start listening for connections
server_socket.listen()

# The main server loop
while True:
  # Accept a connection from a client
  client_socket, client_address = server_socket.accept()
  
  # Create a ClientHandler thread to handle communication with the client
  client_handler = ClientHandler(client_socket, client_address)
  client_handler.start()
  
  # Add the client to the list of clients
  clients.append(client_handler)

