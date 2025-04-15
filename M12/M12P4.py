def load_data():
    lastnames = []
    batting_averages = []
    with open("playerBA.txt", 'r') as file:
        for line in file:
            lastname, batting_average = line.strip().split('-')
            lastnames.append(lastname)
            batting_averages.append(float(batting_average))
        return lastnames, batting_averages


def display_players (lastnames, batting_averages):
    print ("Lastnames and Batting Averages:")
    for i in range(len(lastnames)):
        print(f"{lastnames[i]} - {batting_averages[i]:.3f}")

lastnames, batting_averages = load_data()
display_players(lastnames, batting_averages)

def search_player(lastnames, batting_averages, name):
    for i in range(len(lastnames)):
        if lastnames[i].lower() == name.lower():
            print(f"Found: {lastnames[i]} - {batting_averages[i]:.3f}")
            return
    print("Player not found")

while True:
    name = input("Enter the player's last name to search (or 'exit' to quit): ")
    if name.lower() == 'exit':
        break
    search_player(lastnames, batting_averages, name)