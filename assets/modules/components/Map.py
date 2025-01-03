from assets.modules.components.Player import Player
from assets.modules.elements.constructs.Construct import Construct

class Map:
    def __init__(self, size, color, homes, elements):
        self.size = size
        self.color = color
        self.homes = homes
        self.elements = elements

    def get_home(self, playerId):
        return list(self.homes[playerId])

    def get_elements(self, players: list[Player]):
        elements = []
        for typ, data in self.elements:
            if issubclass(typ, Construct):
                elements.append(typ(players[data[0]], data[1]))
            else:
                elements.append(typ(*data))
        return elements
