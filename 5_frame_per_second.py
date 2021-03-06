import pygame

pygame.init() # 초기화 (반드시)

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("123 Game")

#FPS
clock = pygame.time.Clock()


# 배경이미지 불러오기
background = pygame.image.load("C:\\Users\\nick0\\Desktop\\my_project\\pygame_test\\background.png")


# 캐릭터 불러오기
character = pygame.image.load("C:\\Users\\nick0\\Desktop\\my_project\\pygame_test\\character.png")
character_size = character.get_rect().size  #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60)

    print(" fps: " + str(clock.get_fps()))

    # 캐릭터가 100만큼 이동을 해야한다 ->
    # 10 fps : 1초동안에 10번 동작
    # 20 fps : 1초동안에 20번 동작



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))
    # screen.fill((0, 0, 255))

    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()
