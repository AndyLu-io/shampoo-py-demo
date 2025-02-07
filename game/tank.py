import pygame
import random
import math

# 初始化 pygame
pygame.init()

# 游戏窗口尺寸
width = 800
height = 600
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("坦克大战")

# 游戏颜色
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (213, 50, 80)
blue = (50, 153, 213)
yellow = (255, 255, 102)

# 游戏时钟
clock = pygame.time.Clock()

# 坦克速度
tank_speed = 5
bullet_speed = 10
enemy_speed = 3

# 坦克类
class Tank:
    def __init__(self, x, y, color, direction):
        self.x = x
        self.y = y
        self.color = color
        self.direction = direction  # 方向 0: 上, 1: 右, 2: 下, 3: 左
        self.health = 100

    def move(self):
        if self.direction == 0:  # 上
            self.y -= tank_speed
        elif self.direction == 1:  # 右
            self.x += tank_speed
        elif self.direction == 2:  # 下
            self.y += tank_speed
        elif self.direction == 3:  # 左
            self.x -= tank_speed

    def draw(self):
        pygame.draw.rect(game_window, self.color, [self.x, self.y, 40, 40])

# 子弹类
class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.width = 5
        self.height = 10
        self.speed = bullet_speed

    def move(self):
        if self.direction == 0:
            self.y -= self.speed
        elif self.direction == 1:
            self.x += self.speed
        elif self.direction == 2:
            self.y += self.speed
        elif self.direction == 3:
            self.x -= self.speed

    def draw(self):
        pygame.draw.rect(game_window, yellow, [self.x, self.y, self.width, self.height])

# 创建敌方坦克
class EnemyTank:
    def __init__(self):
        self.x = random.randint(100, width - 100)
        self.y = random.randint(100, height - 100)
        self.color = red
        self.direction = random.randint(0, 3)
        self.health = 50

    def move(self):
        if self.direction == 0:
            self.y -= enemy_speed
        elif self.direction == 1:
            self.x += enemy_speed
        elif self.direction == 2:
            self.y += enemy_speed
        elif self.direction == 3:
            self.x -= enemy_speed

    def draw(self):
        pygame.draw.rect(game_window, self.color, [self.x, self.y, 40, 40])

# 游戏主函数
def gameLoop():
    # 玩家坦克初始位置
    player_tank = Tank(width / 2 - 20, height - 60, green, 0)

    # 存储子弹和敌人
    bullets = []
    enemies = [EnemyTank() for _ in range(5)]  # 初始敌人数量为5

    game_over = False

    while not game_over:
        game_window.fill(blue)  # 背景颜色

        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # 获取按键输入
        keys = pygame.key.get_pressed()

        # 控制玩家坦克的移动
        if keys[pygame.K_UP]:
            player_tank.direction = 0
            player_tank.move()
        if keys[pygame.K_RIGHT]:
            player_tank.direction = 1
            player_tank.move()
        if keys[pygame.K_DOWN]:
            player_tank.direction = 2
            player_tank.move()
        if keys[pygame.K_LEFT]:
            player_tank.direction = 3
            player_tank.move()

        # 发射子弹
        if keys[pygame.K_SPACE]:
            bullet = Bullet(player_tank.x + 15, player_tank.y, player_tank.direction)
            bullets.append(bullet)

        # 子弹移动
        for bullet in bullets:
            bullet.move()
            bullet.draw()

        # 删除出屏幕的子弹
        bullets = [bullet for bullet in bullets if bullet.y > 0 and bullet.x > 0 and bullet.y < height and bullet.x < width]

        # 绘制玩家坦克
        player_tank.draw()

        # 移动和绘制敌人
        for enemy in enemies:
            enemy.move()
            enemy.draw()

        # 检查敌人与玩家子弹碰撞
        for enemy in enemies:
            for bullet in bullets:
                if (enemy.x < bullet.x < enemy.x + 40) and (enemy.y < bullet.y < enemy.y + 40):
                    enemy.health -= 10
                    bullets.remove(bullet)
                    if enemy.health <= 0:
                        enemies.remove(enemy)
                        enemies.append(EnemyTank())  # 生成新的敌人

        pygame.display.update()  # 更新显示

        # 控制游戏帧率
        clock.tick(30)

    pygame.quit()
    quit()

# 启动游戏
gameLoop()
