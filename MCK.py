import pygame
import sys
import random
pygame.init()
pygame.display.set_caption("MCK RESCUES TLINH")
screen = pygame.display.set_mode((1080,768))
clock = pygame.time.Clock()
x_velocity = 6.8
y_velocity = 7
score = 0
highscore = 0
sound1 = pygame.mixer.Sound('AO.wav')
sound2 = pygame.mixer.Sound('LIT.wav')
sound3 = pygame.mixer.Sound('PHULE.wav')
WHITE = (255, 255, 255)
font = pygame.font.Font("04B_19.ttf", 40)
font_over = pygame.font.Font("04B_19.ttf", 60)
pausing = False
jump = False
#tạo hàm cho trò chơi
def draw_floor():
    screen.blit(floor, (floor_x_pos, 600))
    screen.blit(floor, (floor_x_pos + 432, 600))
    screen.blit(floor, (floor_x_pos + 864, 600))
def create_char():
    mck_rect = screen.blit(character, (char_x, char_y))
    return mck_rect
def cal_score():
    score_txt = font.render("Score:" + str(int(score)), True, WHITE)
    screen.blit(score_txt, (5,5))
    highscore_txt = font.render("High Score:" + str(int(highscore)), True, WHITE)
    screen.blit(highscore_txt, (800,5))
def update_score(score, highscore):
    if score > highscore:
        highscore = score
    return highscore  
#chen background
background = pygame.image.load("assets/background-night.png")
background = pygame.transform.scale2x(background)
floor = pygame.image.load("assets/floor.png")
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
background_x_pos = 0
#ve ong cong
DEFAULT_IMAGE_SIZE = (190, 210)
DEFAULT_IMAGE_SIZE2 = (210, 250)
DEFAULT_IMAGE_SIZE3 = (260, 240)
DEFAULT_IMAGE_SIZE4 = (220, 250)
pipe_surface = pygame.image.load("assets/pipe-green.png")
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_surface3 = pygame.image.load("MILOS.png")
pipe_surface3 = pygame.transform.scale2x(pipe_surface3)
pipe_surface3 = pygame.transform.scale(pipe_surface3, DEFAULT_IMAGE_SIZE)
pipe_surface4 = pygame.image.load("WRXDIE.png")
pipe_surface4 = pygame.transform.scale2x(pipe_surface4)
pipe_surface4 = pygame.transform.scale(pipe_surface4, DEFAULT_IMAGE_SIZE2)
pipe_surface5 = pygame.image.load("MEME.png")
pipe_surface5 = pygame.transform.scale2x(pipe_surface5)
pipe_surface5 = pygame.transform.scale(pipe_surface5, DEFAULT_IMAGE_SIZE)
pipe_surface6 = pygame.image.load("ZHONG_XINA.png")
pipe_surface6 = pygame.transform.scale2x(pipe_surface6)
pipe_surface6 = pygame.transform.scale(pipe_surface6, DEFAULT_IMAGE_SIZE4)
pipe_surface7 = pygame.image.load("TRAVIS_SCOTT.png")
pipe_surface7 = pygame.transform.scale2x(pipe_surface7)
pipe_surface7 = pygame.transform.scale(pipe_surface7, DEFAULT_IMAGE_SIZE2)
pipe_surface8 = pygame.image.load("BANH.png")
pipe_surface8 = pygame.transform.scale2x(pipe_surface8)
pipe_surface8 = pygame.transform.scale(pipe_surface8, DEFAULT_IMAGE_SIZE2)
pipe_x = 1000
pipe_height = [390]
pipe_y = random.choice(pipe_height)
#ve nhan vat:
DEFAULT_IMAGE_SIZE1 = (120, 120)
character = pygame.image.load("picwish.png").convert_alpha()
character = pygame.transform.scale(character, DEFAULT_IMAGE_SIZE1)
char_x = 30
char_y = 483
#tạo vị trí bất kì:
list = [pipe_surface, pipe_surface3, pipe_surface4, pipe_surface5, pipe_surface6, pipe_surface7, pipe_surface8]
random_ob = random.choice(list)
pygame.mixer.Sound.play(sound3)
sound3.set_volume(0.5)
while True:
    if 483 >= char_y >= 80:
        if jump == True:
            char_y -= y_velocity
    else:
        jump = False
    if char_y < 483:
        if jump == False:
            char_y += y_velocity
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if char_y == 483:
                    pygame.mixer.Sound.play(sound1)
                    jump = True
                if pausing:
                    background_x_pos = 0
                    char_x = 30
                    char_y = 483
                    pipe_x = 1300
                    pipe_y = random.choice(pipe_height)
                    x_velocity = 6.8
                    y_velocity = 7
                    highscore = update_score(score, highscore)
                    score = 0
                    pausing = False
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pipe_x -= x_velocity
    floor_x_pos -= x_velocity
    background_x_pos -= x_velocity
    screen.blit(background, (background_x_pos,0))
    screen.blit(background, (background_x_pos + 432,0))
    screen.blit(background, (background_x_pos + 864,0))
    create_char()
    pipe_rect = screen.blit(random_ob, (pipe_x,pipe_y))
    mck_rect = screen.blit(character, (char_x, char_y)) 
    if pipe_rect.colliderect(mck_rect):
        pygame.mixer.Sound.play(sound2)
        sound2.set_volume(0.5)
        pausing = True
        gameover_txt = font_over.render("MCK HAS LOST TLINH TO WRXDIE", True, WHITE)
        screen.blit(gameover_txt, (100,200))
        x_velocity = 0
        y_velocity = 0
    draw_floor()
    cal_score()
    if pipe_x + 400 <= 0:
        pipe_x = 1090
        random_ob = random.choice(list)
        score += 1
    if background_x_pos <= -100:
        background_x_pos = 0
    if floor_x_pos <= -300:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)
    