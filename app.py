import pygame,sys,math,random
import client

# DISPLAY SETTINGS
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
PLAYER_RADIUS = 30
FPS = 30




# game variables
players = {}
food = []
player_id = -1
pos_x = -1
pos_y = -1
map_width = -1
map_height = -1
step = 10

# Later another options
def keyboard_controll():
    global  pos_y,pos_x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     pos_y -= step
        # if keys[pygame.K_s]:
        #     pos_y += step
        # if keys[pygame.K_a]:
        #     pos_x -= step
        # if keys[pygame.K_d]:
        #     pos_x += step

def mouse_controll():
    global pos_x,pos_y

    (mouse_x,mouse_y) = pygame.mouse.get_pos()
    x = players[player_id].ball.middle.x * SCALE
    y = players[player_id].ball.middle.y * SCALE
    d = math.sqrt((y - mouse_y)**2 + (x -mouse_x)**2)
    pos_x += int(step*(mouse_x - WINDOW_WIDTH/2)/d)
    pos_y += int(step*(mouse_y - WINDOW_HEIGHT/2)/d)
    print(mouse_x,mouse_y)

# init window
pygame.init()
font = pygame.font.SysFont("consolas",10)
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
window.fill((255,255,255))
window.blit(font.render("Loading...",1,(0,0,0)),(WINDOW_WIDTH/2 - 10,WINDOW_HEIGHT/2))

# connect and get fits data
conn = client.Client()
# data taking from start screen later
map_width,map_height,player_id,pos_x,pos_y= conn.connect("Radek","fire")
player_id = str(player_id)

SCALE = WINDOW_HEIGHT/map_height

while True:

    clock.tick(FPS)

    data = conn.send_and_get(pos_x, pos_y)
    players = data['players']
    food = data['food']
    pos_x = players[player_id].ball.middle.x
    pos_y = players[player_id].ball.middle.y

    keyboard_controll()
    mouse_controll()
    """
    Wszystko ponizej obsługuje wyswietlanie gry
    """
    # SCALE = PLAYER_RADIUS / players[player_id].ball.radius

    window.fill((255,255,255))

    # wyswietlanie kolorow
    for f in food:
        x = f.middle.x * SCALE - pos_x*SCALE + WINDOW_WIDTH/2
        y = f.middle.y * SCALE - pos_y*SCALE + WINDOW_HEIGHT/2
        r = f.radius * SCALE
        pygame.draw.circle(window,(123,100,232),(int(x),int(y)),int(r))

    # wyswietlanie graczy
    for p in players:
        x = players[p].ball.middle.x * SCALE - pos_x*SCALE + WINDOW_WIDTH/2
        y = players[p].ball.middle.y * SCALE - pos_y*SCALE + WINDOW_HEIGHT/2
        r = players[p].ball.radius * SCALE
        pygame.draw.circle(window,players[p].color,(int(x),int(y)),int(r))

    pygame.display.flip()


conn.disconnect()
