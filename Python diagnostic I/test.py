import csv

from Room import Room, create_room
from room_reader import read_rooms

def summarize_room(rooms):
    total_rooms = 0
    total_area = 0.0

    floors = {}

    for room in rooms:
        total_rooms += 1
        total_area += room["area"]

        floor = room["floor"]

        if floor in floors:
            floors[floor] += room["area"]
        else:
            floors[floor] = room["area"]

    if not rooms:
        return 0, 0.0, 0.0, {}

    average_area = total_area / total_rooms

    return total_rooms, total_area, average_area, floors

def main():
    with open("rooms.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row)

if __name__ == "__main__":
    main()