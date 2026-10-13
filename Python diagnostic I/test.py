from Room import Room, create_room

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
    rooms = [
        Room(name = "Office", area = 24.5, floor = 1),
        Room(name = "Storage", area = 12.0, floor = 1),
        Room(name = "Meeting", area = 31.5, floor = 2),
        Room(name = "Server", area = 8.0, floor = 2)
    ]

    for room in rooms:
        print(room.isLarge())

    try:
        room = create_room("Office", 0, 0)
    except ValueError:
        print("Invalid area value")

if __name__ == "__main__":
    main()