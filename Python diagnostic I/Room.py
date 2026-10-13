class Room:
    def __init__(self, name, area, floor):
        self.name = name
        self.area = area
        self.floor = floor

    def isLarge(self):
        if self.area > 25:
            return True
        else:
            return False

def Divide(a, b):

    if (a==0 or b == 0):
        raise ValueError('B is less or equal to 0')
    else:
        return a / b

def create_room(name, area, floor):
    if name == '':
        raise ValueError('Room name is empty')
    elif area <= 0:
        raise ValueError('Area is less than 0')
    elif floor < 0:
        raise ValueError('Floor is less than 0')

    return Room(name, area, floor)