import pygame, math
#GOAL: Make a golf game
LENGTH_ONE = 120
LENGTH_TWO = 90
OMEGA = math.pi/15
BALLX = 600
BALLY = 350

pygame.init()
game_display = pygame.display.set_mode((1200,700))
pygame.display.set_caption("Mini Golf")
clock = pygame.time.Clock()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

kite_points = (0,0)

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

# ball = pygame.draw.circle(game_display, WHITE, (0,0), 25)

playing = True
level = 0

while playing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quit()

    game_display.fill(WHITE)

    kite_points = get_kite(math.pi/2, BALLX, BALLY)

    pygame.draw.polygon(game_display, BLACK, ((kite_points[0],kite_points[1]), (kite_points[2], kite_points[3]), (kite_points[4], kite_points[5]), (kite_points[6], kite_points[7])))

    pygame.display.update()

    clock.tick(100)

