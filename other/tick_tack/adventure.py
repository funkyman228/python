# Welcome to the adventure!
print("Welcome to the adventure!")

# Set the starting location
location = "bedroom"

# Main game loop
while True:
  # Print the current location
  print("You are currently in the " + location)
  
  # Print the available actions
  if location == "bedroom":
    print("What would you like to do?")
    print("1. Go to the kitchen")
    print("2. Go to the bathroom")
    print("3. Go outside")
  elif location == "kitchen":
    print("What would you like to do?")
    print("1. Go to the bedroom")
    print("2. Go to the living room")
  elif location == "bathroom":
    print("What would you like to do?")
    print("1. Go to the bedroom")
  elif location == "living room":
    print("What would you like to do?")
    print("1. Go to the kitchen")
    print("2. Go outside")
  elif location == "outside":
    print("What would you like to do?")
    print("1. Go back inside")
  
  # Get the player's choice
  choice = input("> ")
  
  # Handle the player's choice
  if location == "bedroom":
    if choice == "1":
      location = "kitchen"
    elif choice == "2":
      location = "bathroom"
    elif choice == "3":
      location = "outside"
  elif location == "kitchen":
    if choice == "1":
      location = "bedroom"
    elif choice == "2":
      location = "living room"
  elif location == "bathroom":
    if choice == "1":
      location = "bedroom"
  elif location == "living room":
    if choice == "1":
      location = "kitchen"
    elif choice == "2":
      location = "outside"
  elif location == "outside":
    if choice == "1":
      location = "living room"
      
  # End the game if the player goes back inside
  if location == "living room":
    print("You have successfully completed the adventure! Congratulations!")
    break