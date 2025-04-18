def load_players(filename):
  players = {}
  with open(filename, 'r') as file:
      for line in file:
          name, avg = line.strip().split('-')
          players[name] = float(avg)
  return players


def display_players(player_dict):
  print(f"{'Player':<10} {'Batting Avg':>12}")
  print("-" * 24)
  for name, avg in player_dict.items():
      print(f"{name:<10} {avg:>12.3f}")

def lookup_players(player_dict):
    while True:
        name = input("Enter a player's last name (or type 'exit' to quit): ").strip()
        if name.lower() == 'exit':
            break
        elif name in player_dict:
            print(f"{name}'s batting average is {player_dict[name]:.3f}\n")
        else:
            print("Player not found.\n")

players = load_players('playerBA.txt')
display_players(players)
lookup_players(players)