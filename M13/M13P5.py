import math
def calculate_gallons(length, width, height):
    wall_area = 2 * height * (length + width)
    gallons = math.ceil(wall_area / 50)
    return gallons

def collect_room_data():
    rooms = {}
    while True:
        room_name = input("Enter room name (or type 'done' to finish): ").strip()
        if room_name.lower() == 'done':
            break
        try:
            length = float(input("Enter room length (ft): "))
            width = float(input("Enter room width (ft): "))
            height = float(input("Enter room height (ft): "))
            gallons_needed = calculate_gallons(length, width, height)
            rooms[room_name] = gallons_needed
            print(f"{room_name} will need {gallons_needed} gallon(s) of paint.\n")
        except ValueError:
            print("Please enter valid numbers for dimensions.\n")
    return rooms

def display_paint_requirements(rooms):
    print("\nPaint Requirements:")
    print(f"{'Room':<15} {'Gallons Needed':>15}")
    print("-" * 30)
    for room, gallons in rooms.items():
        print(f"{room:<15} {gallons:>15}")
        
room_paint_dict = collect_room_data()
display_paint_requirements(room_paint_dict)