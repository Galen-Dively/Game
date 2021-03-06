import pygame
import time
import EnemyBase
import player

pygame.init()

playerX = 250 # Player X locale
playerY = 250 # Players Y locale
playerSpeed = 2

backgroundX = 0 # Background X locale
backgroundY = 0 # Background Y locale

### LOADS PLAYER IMAGES ###
playerFrontImg = pygame.image.load("Images/Player Images/playerBackOne.png")
playerBackImg = pygame.image.load("Images/Player Images/playerFrontOne.png")
playerLeftImg = pygame.image.load("Images/Player Images/playerLeftOne.png")
playerRightImg = pygame.image.load("Images/Player Images/playerRightOne.png")
playerImgs = [playerBackImg, playerFrontImg, playerRightImg, playerLeftImg]
### LOADS PLAYER IMAGES ###

### LOADS MAP IMAGES ###
testMap = pygame.image.load("Images/Map Images/TEST_MAP.png")
### LOADS MAP IMAGES ###

### LOADS ENEMY IMAGES ###
enemyOneFrontImg = pygame.image.load("Images/Enemy Images/enemyFrontOne.png")
### LOADS ENEMY IMAGES ###

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

def pauseMenu():
    isOpen = False
    if isOpen:
        pass

playerOne = player.PlayerBase(playerX, playerY, screen, playerImgs,
                              backgroundX, backgroundY, playerSpeed)

enemyOne = EnemyBase.Enemy(50, 2, [], False, enemyOneFrontImg, screen, 100, 100) # creates enemy class

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ### KEYBOARD INPUTS AND MOVEMENTS ###
    keys = pygame.key.get_pressed() # gets pressed keys and assigns it TRUE or FALSE
    if keys[pygame.K_w]: # Checks if "w" is pressed

        playerOne.moveUp()

    if keys[pygame.K_s]: # Checks if "s" is pressed

        playerOne.moveDown()

    if keys[pygame.K_a]:

        playerOne.moveLeft()

    if keys[pygame.K_d]:

        playerOne.moveRight()

    if keys[pygame.K_f]: # TROUBLE SHOOTING KEY
        print(playerOne.x, playerOne.y, "\n", playerOne.backgroundX, playerOne.backgroundY)
        time.sleep(1)

    if keys[pygame.K_ESCAPE]:
        pauseMenu()

    ### KEYBOARD INPUTS AND MOVEMENTS ###

    screen.blit(testMap, (playerOne.backgroundX, playerOne.backgroundY))
    enemyOne.update(backgroundX, backgroundY, playerX, playerY)
    playerOne.show()
    pygame.display.update()
pygame.quit()
quit()
