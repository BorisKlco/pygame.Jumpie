import pygame
from sys import exit
from random import randint


def display_score():
    current_time_ms = int(pygame.time.get_ticks() / 500) - gameTime
    score = font.render(f'Score: {current_time_ms}', False, scoreColor)
    scoreBox = score.get_rect(center=(400, 50))
    screen.blit(score, scoreBox)
    return current_time_ms


def enemyMovement(enemyList):
    if enemyList:
        for enemy in enemyList:
            enemy.x -= 4

            if enemy.bottom == 175:
                screen.blit(flySur, enemy)
            else:
                screen.blit(snailSur, enemy)

        enemyList = [
            seenEnemy for seenEnemy in enemyList if seenEnemy.right > 0
        ]
        return enemyList
    else:
        return []


def collisions(player, enemies):
    if enemies:
        for collision in enemies:
            if player.colliderect(collision):
                return False
    return True


def playerAnimation():
    global playerSur, playerIndex
    if playerBox.bottom < 300:
        playerSur = playerJump
    else:
        playerIndex += 0.1
        if playerIndex >= len(playerWalk):
            playerIndex = 0
        playerSur = playerWalk[int(playerIndex)]


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
finalScore = 0
enemyList = []

skySur = pygame.image.load("assets/Sky.png").convert()
groundSur = pygame.image.load("assets/ground.png").convert()
titleText = font.render('Jumpie!', False, scoreColor)
titleTextBox = titleText.get_rect(center=(400, 75))
instructionText = font.render('Smash  Space  for jump!', False, scoreColor)
instructionTextBox = instructionText.get_rect(center=(400, 350))

snailFrame_1 = pygame.image.load("assets/snail/snail1.png").convert_alpha()
snailFrame_2 = pygame.image.load("assets/snail/snail2.png").convert_alpha()
snailFrame = [snailFrame_1, snailFrame_2]
snailFrameIndex = 0
snailSur = snailFrame[snailFrameIndex]

flyFrame_1 = pygame.image.load("assets/fly/Fly1.png").convert_alpha()
flyFrame_2 = pygame.image.load("assets/fly/Fly2.png").convert_alpha()
flyFrame = [flyFrame_1, flyFrame_2]
flyFrameIndex = 0
flySur = flyFrame[flyFrameIndex]

playerWalk_1 = pygame.image.load(
    "assets/player/player_walk_1.png").convert_alpha()
playerWalk_2 = pygame.image.load(
    "assets/player/player_walk_2.png").convert_alpha()
playerWalk = [playerWalk_1, playerWalk_2]
playerIndex = 0
playerJump = pygame.image.load("assets/player/player_jump.png").convert_alpha()

playerSur = playerWalk[playerIndex]
playerBox = playerSur.get_rect(midbottom=(75, 300))
playerStand = pygame.image.load(
    'assets/player/player_stand.png').convert_alpha()
playerStand = pygame.transform.rotozoom(playerStand, 0, 2)
playerStandBox = playerStand.get_rect(center=(400, 200))

customEventTimer = pygame.USEREVENT + 1
pygame.time.set_timer(customEventTimer, 2000)

snailEventTimer = pygame.USEREVENT + 2
pygame.time.set_timer(snailEventTimer, 500)

flyEventTimer = pygame.USEREVENT + 3
pygame.time.set_timer(flyEventTimer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if gameActive:
                if jumpCount < 2:
                    if event.key == pygame.K_SPACE:
                        playerGrav = -5
                        jumpCount += 1
            else:
                if event.key == pygame.K_SPACE:
                    gameActive = True
                    gameTime = int(pygame.time.get_ticks() / 500)

        if gameActive:
            if event.type == customEventTimer:
                if randint(0, 2):
                    enemyList.append(
                        snailSur.get_rect(bottomleft=(randint(800, 1100),
                                                      300)))
                else:
                    enemyList.append(
                        flySur.get_rect(bottomleft=(randint(1200, 1600), 175)))
            if event.type == snailEventTimer and flyEventTimer:
                if snailFrameIndex == 0 and flyFrameIndex == 0:
                    snailFrameIndex = 1
                    flyFrameIndex = 1
                else:
                    snailFrameIndex = 0
                    flyFrameIndex = 0
                snailSur = snailFrame[snailFrameIndex]
                flySur = flyFrame[flyFrameIndex]

    if gameActive == True:
        screen.blit(skySur, (0, 0))
        screen.blit(groundSur, (0, 300))
        finalScore = display_score()
        enemyList = enemyMovement(enemyList)

        playerGrav += 0.25
        playerBox.y += playerGrav
        if playerBox.bottom >= 300:
            jumpCount = 0
            playerBox.bottom = 300
        playerAnimation()
        screen.blit(playerSur, playerBox)

        game_collisions = gameActive = collisions(playerBox, enemyList)

    else:
        enemyList = []
        playerGrav = 0
        playerBox.bottom = 300
        screen.fill(mainColor)
        screen.blit(playerStand, playerStandBox)
        screen.blit(titleText, titleTextBox)
        finalScoreText = font.render(f'Score: {finalScore}', False, scoreColor)
        finalScoreBox = finalScoreText.get_rect(center=(400, 325))
        if finalScore > 0:
            instructionTextBox.y = 350
            screen.blit(finalScoreText, finalScoreBox)
            screen.blit(instructionText, instructionTextBox)
        else:
            instructionTextBox.y = 325
            screen.blit(instructionText, instructionTextBox)

    pygame.display.update()
    clock.tick(60)
