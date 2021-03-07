import random
import pygame
pygame.init()

class Enemy:
    def __init__(self, health, damage, loot, isDead, image, surface, x, y):
        self.health = health
        self.damage = damage
        self.loot = loot
        self.isDead = isDead
        self.image = image
        self.screen = surface
        self.x = x
        self.y = y

    def attack(self):
        pass

    def dropLoot(self):
        pass

    def update(self, backgroundX, backgroundY, playerX, playerY):
        self.screen.blit(self.image, (self.x, self.y))

