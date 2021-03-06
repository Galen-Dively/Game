import pygame

class PlayerBase:
    def __init__(self, x, y, screen, images, backgroundX, backgroundY, speed):
        self.x = x
        self.y = y
        self.screen = screen
        self.images = images
        self.image = images[0]
        self.backgroundX = backgroundX
        self.backgroundY = backgroundY
        self.speed = speed

    def moveUp(self):
        if self.y == 250:
            if self.backgroundY < 0:
                self.backgroundY += self.speed
        if self.backgroundY >= 0 or self.y > 250:
            self.y -= self.speed
        if self.y <= 0:
            self.y = 0

        self.image = self.images[1]

    def moveDown(self):
        if self.y == 250:
            if self.backgroundY > -500:
                self.backgroundY -= self.speed
        if self.backgroundY <= -500 or self.y < 250:
            self.y += self.speed
        if self.y >= 484:
            self.y = 484
        self.image = self.images[0]

    def moveRight(self):
        if self.x == 250:
            if self.backgroundX > -500:
                self.backgroundX -= self.speed
        if self.backgroundX <= -500 or self.x < 250:
            self.x += self.speed
        if self.x >= 484:
            self.x = 484
        self.image = self.images[2]

    def moveLeft(self):
        if self.x == 250:
            if self.backgroundX < 0:
                self.backgroundX += self.speed
        if self.backgroundX >= 0 or self.x > 250:
            self.x -= self.speed
        if self.x <= 0:
            self.x = 0
        self.image = self.images[3]

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))
