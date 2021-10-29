# Used for clearing the console.
import os

from art_2 import logo

more_players = True
player_list = []
player_id = 1

while more_players:
  print(logo)
  name = str(input("What is your name? \n"))
  secret_bid = float(input("What is your bid? \n$"))

  player_list.append({"id": player_id,"name": name, "bid": secret_bid})
  # accounting for players with the same name. I will be assigning them an ID
  
  print(f"Thank you for your bid {player_list[-1]['name']} Your assigned ID is {player_list[-1]['id']}")
  
  player_id += 1

  incorrect_response = True
  while incorrect_response:
    more_bidders = input("Are there more players?  'Y' or 'N' \n").lower()
    if more_bidders == "y":
      incorrect_response = False
    elif more_bidders == "n":
      incorrect_response = False
      more_players = False

  # Clear the console
  os.system('cls' if os.name == 'nt' else 'clear') 

# start with a null player
# I chose to use a list because I wanted to account for ties.
current_winner = [{"id": 0, "name": "null_player", "bid": -1}]

for id, dict in enumerate(player_list):
    # Checking for ties
    if current_winner[0]["bid"] == dict["bid"]:
      current_winner.append(dict)
    # Checking for winner
    elif current_winner[0]["bid"] < dict["bid"]:
      current_winner = []
      current_winner.append(dict)

for winner in current_winner:
  print(f"{winner['name']}, ID number: {winner['id']}, had a bid of ${winner['bid']:.2f}. \n")
print("Congratulations!")






