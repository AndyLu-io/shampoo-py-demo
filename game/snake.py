import pygame
import time
import random

# 初始化 pygame
pygame.init()

# 游戏窗口尺寸
width = 600
height = 400
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")

# 游戏颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
gray = (169, 169, 169)

# 游戏时钟
clock = pygame.time.Clock()

# 蛇的基本参数
snake_block = 20  # 每个蛇块的大小
snake_speed = 15

# 字体设置
font_style = pygame.font.SysFont("bahnschrift", 35)
score_font = pygame.font.SysFont("comicsansms", 35)

# 显示得分
def your_score(score):
    value = score_font.render("得分: " + str(score), True, black)
    game_window.blit(value, [0, 0])

# 蛇的功能：绘制蛇
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, green, [x[0], x[1], snake_block, snake_block])

# 显示信息
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [width / 6, height / 3])

# 游戏主函数
def gameLoop():
    game_over = False
    game_close = False

    # 蛇的初始位置
    x1 = width / 2
    y1 = height / 2

    # 蛇的移动速度
    x1_change = 0
    y1_change = 0

    # 蛇的长度
    snake_List = []
    Length_of_snake = 1

    # 食物的位置
    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close:
            game_window.fill(blue)  # 背景填充
            message("你输了！按 C 再玩或 Q 退出", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            # 检查用户是否按下了C或Q键
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # 确保蛇不越界
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_window.fill(gray)  # 设置游戏背景为灰色

        # 绘制食物
        pygame.draw.rect(game_window, yellow, [foodx, foody, snake_block, snake_block])

        # 蛇的更新
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # 检查蛇是否撞到自己
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        # 蛇吃到食物
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# 启动游戏
gameLoop()
