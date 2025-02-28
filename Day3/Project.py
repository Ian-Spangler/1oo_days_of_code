print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")
left_right = input(
    "You're at a cross road. Where do you want to go? Type 'left' or 'right'.\n"
).lower()
if left_right == "left":
  swim_wait = input(
      "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n"
  ).lower()
  if swim_wait == "wait":
    door = input(
        "You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
    ).lower()
    if door == "yellow":
      print("You Win!")
    elif door == "red":
      print("Burned by fire. Game Over.")
    elif door == "blue":
      print("Eaten by beasts. Game Over.")
    else:
      print("Game Over.")
  else:
    print("Attacked by trout. Game Over.")
else:
  print("Fall into a hole. Game Over.")
