
import pygame
import random
import math
pygame.init()
#分辨率
X=1366
Y=768
screen = pygame.display.set_mode((1366,768))
#窗口名称
pygame.display.set_caption("t1")
#左上角图标
icon = pygame.image.load("cursor.png")
pygame.display.set_icon(icon)
#背景
bgImg = pygame.image.load("bg.jpg")


#玩家
playerImg = pygame.image.load("aeroshuttle_original.png")
playerX = 400
playerY = 650
playerLStep = 0
playerRStep = 0

#玩家行为
def move_player():

    global playerX

    #绘制玩家位置
    screen.blit(playerImg,(playerX,playerY))

    #移动
    playerX += (playerLStep+playerRStep)

    #边界控制
    if playerX > 1284:
        playerX = 1284
    if playerX < 0:
        playerX = 0


#敌人
class Enemy():
    def __init__(self):
        self.enemyImg = pygame.image.load("nav_buoy_old.png")
        self.enemyX = random.randint(0,X-64)
        self.enemyY = random.randint(100,170)
        self.enemyStep = 1
    #重生
    def respawn(self):
        self.enemyX = random.randint(0,1302)
        self.enemyY = random.randint(100,170)

#敌人数量
number_of_enemies = 6
enemies = []
for i in range(number_of_enemies):
    enemies.append(Enemy())

   
#敌人行为
def move_enemy():
    for e in enemies:
        #绘制敌人
        screen.blit(e.enemyImg,(e.enemyX,e.enemyY))

        #移动
        e.enemyX += e.enemyStep

        #边界控制
        if e.enemyX > 1302 or e.enemyX < 0:
            e.enemyStep *= -1
            e.enemyY += 20

#子弹
class Bullet():
    def __init__(self):
        self.bulletImg = pygame.image.load("missile_harpoon.png")
        self.bulletX = playerX + 35
        self.bulletY = playerY - 26
        self.bulletStep = 5

    def hit(self):
        for e in enemies:
            if(distance(self.bulletX,self.bulletY,e.enemyX,e.enemyY)<20):
                bullets.remove(self)
                e.respawn()

#保存现有子弹
bullets = []

#子弹行为
def move_bullet():
    for b in bullets:
        screen.blit(b.bulletImg,(b.bulletX,b.bulletY))
        b.hit()
        b.bulletY -= b.bulletStep
        if b.bulletY < 0:
            bullets.remove(b)

#测距
def distance(bulletX,bulletY,enemyX,enemyY):
    a = bulletX - enemyX
    b = bulletY - enemyY
    return math.sqrt(a * a + b * b)

#游戏
running = True

while running:

    #加载背景
    screen.blit(bgImg,(0,0))

    #活动
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerRStep = 5
            elif event.key == pygame.K_LEFT:
                playerLStep = -5
            elif event.key == pygame.K_SPACE:
                bullets.append(Bullet())
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                playerRStep = 0
            elif event.key == pygame.K_LEFT:
                playerLStep = 0

    #行为函数调用
    move_player()
    move_enemy()
    move_bullet()

    #刷新窗口
    pygame.display.flip()