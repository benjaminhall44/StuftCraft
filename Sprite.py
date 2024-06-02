from SpriteLib import textures
class Sprite:
    def __init__(self, id: int, x: int, y: int):
        self.id = id
        self.x = x
        self.y = y

    def draw(self, screen, view):
        position = int(self.x - view.x), int(self.y - view.y)
        screen.blit(self.get_texture(), position)

    def get_texture(self):
        return textures[self.id]
