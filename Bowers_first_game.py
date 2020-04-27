import pygame, math
#GOAL: Make a golf game
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
LENGTH_ONE = 80
LENGTH_TWO = 60
OMEGA = math.pi/15


ballx = int(SCREEN_WIDTH/2)
bally = int(SCREEN_HEIGHT/2)
ball_x_acceleration = 20
ball_y_acceleration = 20


pygame.init()
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Golf")
clock = pygame.time.Clock()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

kite_points = ()

def game_quit():
    pygame.quit()
    quit()

def get_kite(angle, x, y):
    tip_x = LENGTH_ONE*math.cos(angle) + x
    tip_y = -(LENGTH_ONE*math.sin(angle)) + y

    right_x = LENGTH_TWO*math.cos(angle-OMEGA) + x
    right_y = -(LENGTH_TWO*math.sin(angle-OMEGA)) + y

    left_x = LENGTH_TWO*math.cos(angle+OMEGA) + x
    left_y = -(LENGTH_TWO*math.sin(angle+OMEGA)) + y
    point_array = []
    point_array.append(x)
    point_array.append(y)
    point_array.append(left_x)
    point_array.append(left_y)
    point_array.append(tip_x)
    point_array.append(tip_y)
    point_array.append(right_x)
    point_array.append(right_y)
    point_array.append(x)
    point_array.append(y)
    
    return point_array

def ball_acceleration(cur_ball_x, cur_ball_y, ball_x_acceleration, ball_y_acceleration):
    if ball_x_acceleration > 0:
        ball_x_acceleration -= 1
    elif ball_x_acceleration < 0:
        ball_x_acceleration += 1

    if ball_y_acceleration > 0:
        ball_y_acceleration -= 1
    elif ball_y_acceleration < 0:
        ball_y_acceleration += 1
    
    new_x = cur_ball_x+ball_x_acceleration
    new_y = cur_ball_y+ball_y_acceleration

    return new_x, new_y, ball_x_acceleration, ball_y_acceleration

def draw_ball(x,y):
    pygame.draw.circle(game_display, WHITE, (x,y), 10)

playing = True
level = 0

while playing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quit()

    game_display.fill(GREEN)

    ballx, bally, ball_x_acceleration, ball_y_acceleration = ball_acceleration(ballx, bally, ball_x_acceleration, ball_y_acceleration)
    draw_ball(ballx, bally)

    kite_points = get_kite(math.pi/2, ballx, bally)
    pygame.draw.polygon(game_display, BLACK, ((kite_points[0],kite_points[1]), (kite_points[2], kite_points[3]), (kite_points[4], kite_points[5]), (kite_points[6], kite_points[7])))

    pygame.display.update()

    clock.tick(60)