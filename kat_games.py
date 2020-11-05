import pygame
import random

pygame.init()
win = pygame.display.set_mode((1200, 720))
pygame.display.set_caption('Kat Games')
clock = pygame.time.Clock()

bg = pygame.image.load('background.png')

score = 0


x_kat, y_kat = 500, 562
left = False
right = False

isJump = False
jumpCount = 10

animCount = 0
animAttack = 0
isAttack = False

playerStand = pygame.image.load('to_right.png')
playerRight = [pygame.image.load('to_right.png'), pygame.image.load('to_right_2.png'),
               pygame.image.load('to_right_3.png'),
               pygame.image.load('to_right_4.png'), pygame.image.load('to_right_5.png'),
               pygame.image.load('to_right_6.png')]
playerLeft = [pygame.image.load('to_left.png'), pygame.image.load('to_left_2.png'), pygame.image.load('to_left_3.png'),
              pygame.image.load('to_left_4.png'), pygame.image.load('to_left_5.png'),
              pygame.image.load('to_left_6.png')]

Walk_Right_Atacck = [pygame.image.load('attack_right_1.png'), pygame.image.load('attack_right_2.png'),
                     pygame.image.load('attack_right_3.png'), pygame.image.load('attack_right_4.png'),
                     pygame.image.load('attack_right_5.png')]
Walk_Left_Atacck = [pygame.image.load('attack_left_1.png'), pygame.image.load('attack_left_2.png'),
                    pygame.image.load('attack_left_3.png')]


def kat():
    global animCount, animAttack,left,right,isAttack,x_kat,y_kat,isJump,jumpCount

    win.blit(bg, (0, 0))
    if animAttack + 1 >= 25:
        animAttack = 0

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(playerLeft[animCount // 5], (x_kat, y_kat))
        animCount += 1

    elif right:
        win.blit(playerRight[animCount // 5], (x_kat, y_kat))
        animCount += 1

    elif isAttack:
        win.blit((Walk_Right_Atacck)[animAttack // 5], (x_kat, y_kat))
        animAttack += 1

    else:
        if right:
            win.blit(pygame.image.load('to_right.png'), (x_kat, y_kat))
        elif left:
            win.blit(pygame.image.load('to_left.png'), (x_kat, y_kat))
        else:
            win.blit(pygame.image.load('to_right.png'), (x_kat, y_kat))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        left = True
        right = False
        if x_kat >= 0:
            x_kat -= 10
    elif keys[pygame.K_d]:
        right = True
        left = False
        if x_kat <= 1110:
            x_kat += 10

    elif keys[pygame.K_LSHIFT]:
        isAttack = True
        left = False
        right = False

    else:
        left = False
        right = False
        animAttack = 0
        isAttack = False
        animCount = 0

    if keys[pygame.K_SPACE]:
        isJump = True
    if isJump:
        if jumpCount >= -10:
            if jumpCount < 0:
                y_kat += (jumpCount ** 2) / 2
            else:
                y_kat -= (jumpCount ** 2) / 2
            jumpCount -= 0.5
        else:
            isJump = False
            jumpCount = 10

    pygame.display.update()


def print_text(message, x, y, font_color=(0, 0, 0), font_type='PingPong.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    win.blit(text, (x, y))
    pygame.display.update()


def position_check(x, y):
    if y + 40 >= y_kat >= y - 100:
        if x - 70 <= x_kat and x + 30 >= x_kat:
                return True
    return False

# def test():
#     health_skin = pygame.image.load('жизнь.png')
#     healt_x = 650
#     healt_y = 550
#     win.blit(health_skin, (healt_x,healt_y))
#     if position_check(healt_x,healt_y):
#         win.blit(health_skin,(500,200))
#     pygame.display.update()
class Health:
    def __init__(self):
        self.healt_x = 3500
        self.healt_y = 3500
        self.num_heal = 150

    def move_help(self):
        self.health_skin = pygame.image.load('жизнь.png')
        win.blit(self.health_skin, (self.healt_x, self.healt_y))
        self.healt_x -= 6
        self.healt_y -= random.randint(45, 50)
        self.healt_y += random.randint(45, 50)
        if self.healt_y >= 450:
            self.healt_y -= 25
        if self.healt_y <= 220:
            self.healt_y += 25
        if self.healt_x <= -1500 or position_check(self.healt_x, self.healt_y):
            self.num_heal += 50
            self.healt_x = random.randint(3500, 5500)
        pygame.display.update()

    def number_health(self):
        for n in range(0,self.num_heal,50):
            win.blit(self.health_skin,(n,40))
        pygame.display.update()

health = Health()


stone_x, stone_y = random.randint(0, 1200), -100
def stones():
    global stone_x, stone_y
    stones_skin = pygame.image.load('stones.png')
    win.blit(stones_skin, (stone_x, stone_y))
    stone_y += random.randint(6, 15)
    if stone_y >= 650:
        stone_y = -random.randint(500, 1000)
        stone_x = random.randint(0, 1200)
    if position_check(stone_x, stone_y):
        health.num_heal -= 6

    pygame.display.update()

class Arrow:

    def __init__(self):
        self.y = 600
        self.route = random.randint(1,2)
        if self.route == 1:
            self.x = random.randint(2000,5000)
        else:
            self.x = - random.randint(1500,3999)

    def arrow_move(self):
        if self.route == 1:
            self.sprite = pygame.image.load('стрела_лево.png')
            self.x -= 10
            if self.x <= -1000:
                self.__init__()
        else:
            self.sprite = pygame.image.load('стрела_право.png')
            self.x += 10
            if self.x >= 2500:
                self.__init__()
        win.blit(self.sprite, (self.x, self.y))

        if position_check(self.x, self.y):
            health.num_heal -= 6

        pygame.display.update()

arrow = Arrow()

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    score += 1
    print_text('score : ' + str(score), x=1000, y=20)
    kat()
    health.move_help()
    health.number_health()
    stones()
    arrow.arrow_move()


pygame.quit()
