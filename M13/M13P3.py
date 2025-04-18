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


players = load_players('playerBA.txt')
display_players(players)