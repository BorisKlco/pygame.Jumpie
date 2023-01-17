import pygame
from sys import exit


def display_score():
    current_time_ms = int(pygame.time.get_ticks() / 500) - gameTime
    score = font.render(f'Score: {current_time_ms}', False, scoreColor)
    scoreBox = score.get_rect(center=(400, 50))
    screen.blit(score, scoreBox)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Jumpie!")
clock = pygame.time.Clock()
font = pygame.font.Font("assets/font/Pixeltype.ttf", 50)
mainColor = "#c0e8ec"
scoreColor = (64, 64, 64)
gameActive = False
playerGrav = 0
jumpCount = 0
gameTime = 0

skySur = pygame.image.load("assets/Sky.png").convert()
groundSur = pygame.image.load("assets/ground.png").convert()
titleText = font.render('Jumpie!', False, scoreColor)
titleTextBox = titleText.get_rect(center=(400, 75))
instructionText = font.render('Smash  Space  for jump!', False, scoreColor)
instructionTextBox = instructionText.get_rect(center=(400, 325))

snailSur = pygame.image.load("assets/snail/snail1.png").convert_alpha()
snailBox = snailSur.get_rect(bottomleft=(800, 300))

playerSur = pygame.image.load(
    "assets/player/player_walk_1.png").convert_alpha()
playerBox = playerSur.get_rect(midbottom=(75, 300))
playerStand = pygame.image.load(
    'assets/player/player_stand.png').convert_alpha()
playerStand = pygame.transform.rotozoom(playerStand, 0, 2)
playerStandBox = playerStand.get_rect(center=(400, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if gameActive == True:
                if jumpCount < 2:
                    if event.key == pygame.K_SPACE:
                        playerGrav = -4
                        jumpCount += 1
            else:
                if event.key == pygame.K_SPACE:
                    gameActive = True
                    gameTime = int(pygame.time.get_ticks() / 500)

    if gameActive == True:
        screen.blit(skySur, (0, 0))
        screen.blit(groundSur, (0, 300))
        display_score()

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

        if snailBox.colliderect(playerBox):
            gameActive = False
            snailBox.left = 800
            playerBox.bottom = 300
    else:
        screen.fill(mainColor)
        screen.blit(playerStand, playerStandBox)
        screen.blit(titleText, titleTextBox)
        screen.blit(instructionText, instructionTextBox)

    pygame.display.update()
    clock.tick(60)
