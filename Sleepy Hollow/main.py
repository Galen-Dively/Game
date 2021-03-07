import pygame
import time
import EnemyBase
import player
import melee

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

### LOADS INVENTORY ICONS ###
emptySlotImg = pygame.image.load("Images/Inventory Images/emptySlot.png")
unselectedWoodSwordImg = pygame.image.load("Images/Inventory Images/woodswordunselected.png")
inventoryImgs = [emptySlotImg, unselectedWoodSwordImg]
### LOADS INVENTORY ICONS ###

### LOADS WEAPON IMAGES ###
woodenSwordImg = pygame.image.load("Images/Weapon Images/woodsword.png")
### LOADS WEAPON IMAGES ###

### LOADS MAP IMAGES ###
testMap = pygame.image.load("Images/Map Images/TEST_MAP.png")
### LOADS MAP IMAGES ###

### LOADS ENEMY IMAGES ###
enemyOneFrontImg = pygame.image.load("Images/Enemy Images/enemyFrontOne.png")
### LOADS ENEMY IMAGES ###

### INVENTORY VARIABLES ###
slotOneContentImg = emptySlotImg
### INVENTORY VARIABLES ###

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

def pauseMenu():
    isOpen = False
    if isOpen:
        pass

woodSword = melee.Melee_Weapon(3, 'common', woodenSwordImg, False, 20, 300, screen)

playerOne = player.PlayerBase(playerX, playerY, screen, playerImgs,
                              backgroundX, backgroundY, playerSpeed, inventoryImgs, woodSword)

enemyOne = EnemyBase.Enemy(50, 2, [], False, enemyOneFrontImg, screen, 100, 100) # creates enemy class

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ### KEYBOARD INPUTS AND MOVEMENTS ###


    keys = pygame.key.get_pressed() # gets pressed keys and assigns it TRUE or FALSE
    if keys[pygame.K_1]:
        playerOne.selectSlot(1)

    if keys[pygame.K_2]:
        playerOne.selectSlot(2)

    if keys[pygame.K_3]:
        playerOne.selectSlot(3)


    if keys[pygame.K_4]:
        playerOne.selectSlot(4)

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

    if keys[pygame.K_e]:
        pass

    if keys[pygame.K_q]:
        playerOne.drop()

    if keys[pygame.K_ESCAPE]:
        pauseMenu()

    ### KEYBOARD INPUTS AND MOVEMENTS ###

    screen.blit(testMap, (playerOne.backgroundX, playerOne.backgroundY))
    enemyOne.update(backgroundX, backgroundY, playerX, playerY)


    ### INVENTORY STUFF ###
    playerOne.inventory()
    ### INVENTORY STUFF ###

    ### WEAPON STUFF ###
    woodSword.show(playerOne) # displays the wood sword image
    ### WEAPON STUFF ###

    ### PLAYER STUFF ###
    playerOne.show(woodSword)
    playerOne.collision(woodSword.weaponRect, woodSword)
    ### PLAYER STUFF ###

    pygame.display.update()
pygame.quit()
quit()
