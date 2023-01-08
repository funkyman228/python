import socket

# Constants for the dimensions of the game board
ROWS = 3
COLUMNS = 3
DEPTH = 3

# The IP address and port of the server
SERVER_ADDRESS = ("10.0.0.1", 8000)

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(SERVER_ADDRESS)

# The main game loop
while True:
  # Receive the game board from the server
  data = client_socket.recv(1024).decode()
  
  # If the server has closed the connection, exit the game loop
  if not data:
    break
  
  # Print the game board
  print(data)
  
  # Get the player's move
  x, y, z = map(int, input("Enter your move (x y z): ").split())
  
  # Send the move to the server
  client_socket.sendall((str(x) + " " + str(y) + " " + str(z)).encode())
  
# Close the client socket
client_socket.close()
