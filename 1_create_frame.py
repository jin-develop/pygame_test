import pygame

pygame.init() # 초기화 (반드시)

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("123 Game")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

# pygame 종료
pygame.quit()
