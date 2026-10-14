import csv


def read_rooms(filename):
    with open(filename, 'r') as file:
        content = csv.DictReader(file)

    print(content)