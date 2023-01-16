import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Jumpie!')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

skySur = pygame.image.load('assets/Sky.png').convert()
groundSur = pygame.image.load('assets/ground.png').convert()
text = font.render('Jumpie!', False, (64, 64, 64))
textBox = text.get_rect(center=(400, 50))

snailSur = pygame.image.load('assets/snail/snail1.png').convert_alpha()
snailBox = snailSur.get_rect(midbottom=(820, 300))

playerSur = pygame.image.load(
    'assets/player/player_walk_1.png').convert_alpha()
playerBox = playerSur.get_rect(midbottom=(100, 300))
playerGrav = 0
jumpCount = 0

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

    screen.blit(skySur, (0, 0))
    screen.blit(groundSur, (0, 300))
    screen.blit(text, textBox)
    snailBox.x -= 5
    if snailBox.right <= 0:
        snailBox.left = 820
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