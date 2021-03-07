class PlayerBase:
    def __init__(self, x, y, screen, images, backgroundX, backgroundY, speed,
                 inventoryImages, woodSword):
        self.x = x
        self.y = y
        self.screen = screen
        self.images = images
        self.image = images[0]
        self.backgroundX = backgroundX
        self.backgroundY = backgroundY
        self.speed = speed

        self.inventoryImg = inventoryImages
        self.slotOneImg = inventoryImages[0]
        self.slotTwoImg = inventoryImages[0]
        self.slotThreeImg = inventoryImages[0]
        self.slotFourImg = inventoryImages[0]

        self.slotOneContent = 0
        self.slotTwoContent = 0
        self.slotThreeContent = 0
        self.slotFourContent = 0

        self.selectedSlot = 1

        self.woodSword = woodSword

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

    def show(self, woodSword):
        self.screen.blit(self.image, (self.x, self.y))

        if woodSword.pickedUp and self.selectedSlot == 1:
            woodSword.x = self.x + 10
            woodSword.y = self.y - 5

    def collision(self, woodSwordRect, woodSword):
        playerRect = self.images[1].get_rect(topleft=(self.x, self.y))
        if playerRect.colliderect(woodSwordRect):
            woodSword.pickedUp = True
            self.slotOneImg = self.inventoryImg[1]
            self.slotOneContent = woodSword

    def inventory(self):
        self.screen.blit(self.slotOneImg, (380, 0))
        self.screen.blit(self.slotTwoImg, (410, 0))
        self.screen.blit(self.slotThreeImg, (440, 0))
        self.screen.blit(self.slotFourImg, (470, 0))

    def selectSlot(self, slot):
        self.selectedSlot = slot

        if self.selectedSlot == 1:
            self.woodSword.show()
        if self.selectedSlot != 1:
            self.woodSword.hide()
        if self.selectedSlot == 2:
            print("2")
        if self.selectedSlot != 2:
            pass

    def drop(self):
        if self.woodSword.pickedUp:
            self.woodSword.pickedUp = False
            self.woodSword.x += 3
            self.woodSword.y += 3
            self.slotOneImg = self.inventoryImg[0]
