import pygame
class Menu:
    Tabs = ("Buildings", "Troops", "Workers", "Machines", "Research")
    Contents = {
        "Buildings": (
            {"Name": "Base", "Cost": 10, "Id": 0},
        ),
        "Troops": (
            {"Name": "Three", "Cost": 3, "Id": 1},
            {"Name": "Four", "Cost": 4, "Id": 2},
            {"Name": "Man", "Cost": 6, "Id": 3},
            {"Name": "LaserEagle", "Cost": 7, "Id": 4},
            {"Name": "BigMan", "Cost": 8, "Id": 5},
            {"Name": "Spider", "Cost": 9, "Id": 6},
            {"Name": "FlyingTank", "Cost": 11, "Id": 7}
        ),
        "Workers": (
            {"Name": "Miner", "Cost": 5, "Id": 8},
        ),
        "Machines": (
            {"Name": "Car", "Cost": 12, "Id": 9},
        ),
        "Research": (
            {"Name": "Dragon", "Cost": 16, "Id": 10},
        )
    }
    MISSED_MENU = 0
    NO_EFFECT = 1
    SCROLL = 2
    SCROLL_TAB = 3
    CHANGE_TAB = 4
    BOUGHT = 5
    TOEXPENSIVE = 6
    CONTROL = 7
    CONTROL_RADIUS_UP = 8
    CONTROL_RADIUS_DOWN = 9

    Textures = {
        "Mineral": pygame.image.load("assets/graphics/menu/mineral.png"),

        "Control": pygame.image.load("assets/graphics/menu/control.png"),

        "LeftScrollArrow": pygame.image.load("assets/graphics/menu/leftscrollarrow.png"),
        "RightScrollArrow": pygame.image.load("assets/graphics/menu/rightscrollarrow.png"),

        "LeftTabScrollArrow": pygame.image.load("assets/graphics/menu/lefttabscrollarrow.png"),
        "RightTabScrollArrow": pygame.image.load("assets/graphics/menu/righttabscrollarrow.png"),

        "Base": pygame.image.load("assets/graphics/menu/icons/buildings/base.png"),

        "Three": pygame.image.load("assets/graphics/menu/icons/troops/three.png"),
        "Four": pygame.image.load("assets/graphics/menu/icons/troops/four.png"),
        "Man": pygame.image.load("assets/graphics/menu/icons/troops/man.png"),
        "LaserEagle": pygame.image.load("assets/graphics/menu/icons/troops/lasereagle.png"),
        "BigMan": pygame.image.load("assets/graphics/menu/icons/troops/bigman.png"),
        "Spider": pygame.image.load("assets/graphics/menu/icons/troops/spider.png"),
        "FlyingTank": pygame.image.load("assets/graphics/menu/icons/troops/flyingtank.png"),

        "Miner": pygame.image.load("assets/graphics/menu/icons/workers/miner.png"),

        "Car": pygame.image.load("assets/graphics/menu/icons/machines/car.png"),

        "Dragon": pygame.image.load("assets/graphics/menu/icons/research/dragon.png")
    }

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)

        self.minerals = 0

        self.tab = 0
        self.tab_scroll = 0
        self.scroll = 0

    def draw_menu(self, screen):
        self.draw_minerals(screen)
        self.draw_controls(screen)
        self.draw_shop(screen)

    def draw_minerals(self, screen):
        screen.blit(self.Textures["Mineral"], [30,30])
        screen.blit(self.font.render(str(self.minerals), 0, self.get_mineral_color()), [70,35])

    def draw_controls(self, screen):
        screen.blit(self.Textures["Control"], [30,90])

    def get_mineral_color(self):
        if self.minerals < 10:
            return (0,0,0)
        elif self.minerals < 100:
            return (0, 255, 255)
        else:
            return (200, 200, 0)

    def get_price_color(self, price):
        if self.minerals < price:
            return (200,0,0)
        else:
            return (0, 200, 200)

    def draw_shop(self, screen: pygame.surface.Surface):
        size = screen.get_rect()[2:4]

        # Draw Tabs
        s = self.tab_scroll
        for i in range(len(self.Tabs)):
            t = self.Tabs[i]
            if i == self.tab:
                pygame.draw.rect(screen, [200, 200, 255], [s, size[1] - 100 - 30, 150, 30])
                pygame.draw.rect(screen, [230, 230, 255], [s, size[1] - 100 - 30, 150, 30], width=3)
                text = self.font.render(t, 0, [0, 50, 50])
                center = [s + 75, size[1] - 100 - 15]
                screen.blit(text, [center[0] - text.get_size()[0]//2, center[1] - text.get_size()[1]//2])
                s += 150
            else:
                pygame.draw.rect(screen, [200, 200, 200], [s, size[1] - 100 - 25, 120, 25])
                pygame.draw.rect(screen, [230, 230, 230], [s, size[1] - 100 - 25, 120, 25], width=3)
                text = self.font.render(t, 0, [0,0,0])
                center = [s + 60, size[1] - 100 - 12]
                screen.blit(text, [center[0] - text.get_size()[0]//2, center[1] - text.get_size()[1]//2])
                s += 120

        if self.tab_scroll < 0:
            screen.blit(self.Textures["LeftTabScrollArrow"], [5, size[1] - 100 - 25])
        if s > size[0]:
            screen.blit(self.Textures["RightTabScrollArrow"], [size[0] - 15, size[1] - 100 - 25])

        # Draw Icons
        pygame.draw.rect(screen, [220,220,220], [0, size[1] - 100, size[0], 100])

        s = self.scroll
        for p in self.Contents[self.Tabs[self.tab]]:
            self.draw_shop_item(screen, [s, size[1] - 100], p["Name"], p["Cost"])
            s += 100

        if self.scroll < 0:
            screen.blit(self.Textures["LeftScrollArrow"], [5, size[1] - 100 + 5])
        if s > size[0]:
            screen.blit(self.Textures["RightScrollArrow"], [size[0] - 25, size[1] - 100 + 5])

    def draw_shop_item(self, screen, dest, name, cost):
        pygame.draw.rect(screen, [100, 100, 100], [dest[0] + 10, dest[1] + 10, 80, 80], width=5)
        texture: pygame.surface.Surface = self.Textures[name]

        screen.blit(texture, [dest[0] + 5, dest[1] + 5])

        screen.blit(self.Textures["Mineral"], [dest[0] + 10, dest[1] + 60])
        screen.blit(self.font.render(str(cost), 0, self.get_price_color(cost)), [dest[0] + 45, dest[1] + 65])

    def click_menu(self, size, location):

        if location[1] > size[1] - 100:
            if self.scroll < 0:
                if 5 < location[0] < 25 and size[1] - 100 + 5 < location[1] < size[1] - 100 + 95:
                    self.scroll += 10
                    return self.SCROLL, None
            if self.scroll + 100 * len(self.Contents[self.Tabs[self.tab]]) > size[0]:
                if size[0] - 25 < location[0] < size[0] - 5 and size[1] - 100 + 5 < location[1] < size[1] - 100 + 95:
                    self.scroll -= 10
                    return self.SCROLL, None

            s = self.scroll
            for p in self.Contents[self.Tabs[self.tab]]:
                if s + 10 < location[0] < s + 90 and size[1] - 100 + 10 < location[1] < size[1] - 100 + 90:
                    return self.BOUGHT, p["Id"]
                s += 100

        if self.tab_scroll < 0:
            if 5 < location[0] < 15 and size[1] - 100 - 25 < location[1] < size[1] - 100:
                self.tab_scroll += 10
                return self.SCROLL_TAB, None

        if self.tab_scroll + 120 * len(self.Tabs) + 30 > size[0]:
            if size[0] - 15 < location[0] < size[0] - 15 + 10 and size[1] - 100 - 25 < location[1] < size[1] - 100:
                self.tab_scroll -= 10
                return self.SCROLL_TAB, None

        s = self.tab_scroll
        for i in range(len(self.Tabs)):
            t = self.Tabs[i]
            if i == self.tab:
                if s < location[0] < s + 150 and size[1] - 100 - 30 < location[1] < size[1] - 100:
                    return self.NO_EFFECT, None
                s += 150
            else:
                if s < location[0] < s + 120 and size[1] - 100 - 25 < location[1] < size[1] - 100:
                    self.tab = i
                    self.scroll = 0
                    return self.CHANGE_TAB, None
                s += 120

        if 30 < location[0] < 60:
            if 90 < location[1] < 120:
                return self.CONTROL, None
            elif 130 < location[1] < 160:
                return self.CONTROL_RADIUS_UP, None
            elif 170 < location[1] < 200:
                return self.CONTROL_RADIUS_DOWN, None

        return self.MISSED_MENU, None
