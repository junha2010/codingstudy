import pygame


pygame.init()

screen_width = 480
screen_heiht = 640
screen = pygame.display.set_mode((screen_width, screen_heiht))
pygame.display.set_caption("Nado Game")

running = True  # 게임이 진행 중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()