import random
class Melee_Weapon:
    def __init__(self, damage, rarity, image, pickedUp, x, y, screen):
        self.damage = damage
        self.rarity = rarity
        self.image = image
        self.pickedUp = pickedUp
        self.x, self.y = x, y
        self.screen = screen
        self.weaponRect = 0

    def attack(self):
        pass

    def show(self, player):
        self.screen.blit(self.image, (self.x, self.y))
        self.weaponRect = self.image.get_rect(topleft=(self.x, self.y))

    def hide(self):
        self.x = 10000
        self.y = 10000
