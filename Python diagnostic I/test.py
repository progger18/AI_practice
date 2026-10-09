# 1. количество помещений
# 2. общую площадь
# 3. среднюю площадь
# 4. суммарную площадь каждого этажа

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