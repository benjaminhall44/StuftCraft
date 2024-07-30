
class Player:
    def __init__(self, name, id, home, minerals):
        self.name = name
        self.id = id
        self.home = home
        self.minerals = minerals
        self.command_centers = 0
        self.selected = []

PLAYING = 2
LOSE = 0
WIN = 1
