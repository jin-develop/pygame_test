import pygame

pygame.init() # 초기화 (반드시)

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("avoid poo")

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

# 적 enemy 캐릭터
enemy = pygame.image.load("C:\\Users\\nick0\\Desktop\\my_project\\pygame_test\\enemy.png")
enemy_size = enemy.get_rect().size  #이미지의 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터의 가로 크기
enemy_height = enemy_size[1]  # 캐릭터의 세로 크기
enemy_x_pos = screen_width / 2 - enemy_width / 2
enemy_y_pos = screen_height / 2 - enemy_height / 2


# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성

# 총 시간
total_time = 10


# 시간 계산
start_ticks = pygame.time.get_ticks()



# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30)

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



    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos


    # 충돌 체크 

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False


    screen.blit(background, (0, 0))
    # screen.fill((0, 0, 255))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))


    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = ( pygame.time.get_ticks() - start_ticks ) / 1000  # 경과 시간(ms)을 1000으로 나누어서 s 로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))

    screen.blit(timer, (10, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃") 
        running = False


    pygame.display.update() # 게임화면을 다시 그리기!

# 잠시 대기
pygame.time.delay(2000) 

# pygame 종료
pygame.quit()
