from SpriteLib import textures, layer_map
class Sprite:
    def __init__(self, id: int, x: int, y: int):
        self.id = id
        self.pos = x,y

    def draw(self, screen, view):
        texture = self.get_texture()
        position = int(self.pos[0] - view[0] - texture.get_size()[0]//2), int(self.pos[1] - view[1] - texture.get_size()[1]//2)
        screen.blit(texture, position)

    def get_texture(self):
        return textures[self.id]

    def get_layer(self):
        return layer_map[self.id]