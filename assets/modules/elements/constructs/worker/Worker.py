from assets.modules.elements.constructs.Construct import *

class Worker (Construct):
    speed: float
    carrying: int
    target: Element
    def travel(self):
        distance = self.walk(self.target.position)
        return distance < (self.radius + self.target.radius)

    def findNearest(self, kind: type, elements: list[Element], owner=None):
        nearest = None
        distance = 2000000
        for e in elements:
            if type(e) is kind:
                if owner is None or (isinstance(e, Construct) and e.player is owner):
                    dist = (e.position[0] - self.position[0]) ** 2 + (e.position[1] - self.position[1]) ** 2
                    if dist < distance:
                        nearest = e
                        distance = dist
        return nearest

