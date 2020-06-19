import pygame

pygame.init() # 초기화 (반드시)

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("123 Game")

# 배경이미지 불러오기
background = pygame.image.load("C:\\Users\\nick0\\Desktop\\my_project\\pygame_test\\background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    # screen.fill((0, 0, 255))
    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()
