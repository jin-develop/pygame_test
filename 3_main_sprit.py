import pygame

pygame.init() # 초기화 (반드시)

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("123 Game")

# 배경이미지 불러오기
background = pygame.image.load("C:\\Users\\nick0\\Desktop\\my_project\\pygame_test\\background.png")


# 캐릭터 불러오기
character = pygame.image.load("C:\\Users\\nick0\\Desktop\\my_project\\pygame_test\\character.png")
character_size = character.get_rect().size  #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height



# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    # screen.fill((0, 0, 255))

    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()
