import pygame
from sys import exit
"""
Content:
|x| Vars,style,settings
  |x| Game assets import
  |x| Classes
    |x| x class
|x| Event loop
  |x| fixed .blit assets
  |x| logic .blit assets

VSTEST
"""

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Jumpie')
clock = pygame.time.Clock()
font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)
mainColor = "#c0e8ec"
scoreColor = (64, 64, 64)
playerGrav = 0
jumpCount = 0

skySur = pygame.image.load('assets/Sky.png').convert()
groundSur = pygame.image.load('assets/ground.png').convert()

score = font.render('Jumpie', False, scoreColor)
scoreBox = score.get_rect(center=(400, 50))

snailSur = pygame.image.load('assets/snail/snail1.png').convert_alpha()
snailBox = snailSur.get_rect(bottomleft=(800, 300))

playerSur = pygame.image.load(
    'assets/player/player_walk_1.png').convert_alpha()
playerBox = playerSur.get_rect(midbottom=(75, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if jumpCount < 2:
                if event.key == pygame.K_SPACE:
                    playerGrav = -4
                    jumpCount += 1

    #baseAssets
    screen.blit(skySur, (0, 0))
    screen.blit(groundSur, (0, 300))
    pygame.draw.rect(screen, mainColor, scoreBox)
    screen.blit(score, scoreBox)

    #gameAssets
    snailBox.x -= 4
    if snailBox.right <= 0:
        snailBox.left = 800
    screen.blit(snailSur, snailBox)

    playerGrav += 0.20
    playerBox.y += playerGrav
    if playerBox.bottom >= 300:
        playerGrav = 0
        jumpCount = 0
        playerBox.bottom = 300
    screen.blit(playerSur, playerBox)

    pygame.display.update()
    clock.tick(60)
