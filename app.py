import pygame, math
import client
from gui.menu import Menu
from game_view.element import Element
from game_view.rank import Rank

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
step = 4


# Later another options
def keyboard_control():
    global pos_y, pos_x
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


def mouse_control():
    global pos_x, pos_y

    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    x = players[player_id].ball.middle.x * SCALE - pos_x * SCALE + WINDOW_WIDTH / 2
    y = players[player_id].ball.middle.y * SCALE - pos_y * SCALE + WINDOW_HEIGHT / 2
    # print(mouse_x,mouse_y,pos_x,pos_y, x, y, players[player_id].ball.middle.x, players[player_id].ball.middle.y)
    d = math.sqrt((mouse_y - y) ** 2 + (mouse_x - x) ** 2)
    if d != 0:
        pos_x += int(step * (mouse_x - WINDOW_WIDTH / 2) / d)
        pos_y += int(step * (mouse_y - WINDOW_HEIGHT / 2) / d)

    if pos_x < 0:
        pos_x = 0
    if pos_y < 0:
        pos_y = 0
    if pos_x > map_width:
        pos_x = map_width
    if pos_y > map_height:
        pos_y = map_height


# init window
pygame.init()
font = pygame.font.SysFont("consolas", 10)
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill((255, 255, 255))
window.blit(font.render("Loading...", 1, (0, 0, 0)), (WINDOW_WIDTH / 2 - 10, WINDOW_HEIGHT / 2))
rank = Rank(window, WINDOW_WIDTH - 150, 0)
# Menu rendering
menu = Menu(window, WINDOW_WIDTH, WINDOW_HEIGHT)
nick_name, element = menu.display()
# connect and get fits data
conn = client.Client()
# data taking from start screen later
map_width, map_height, player_id, pos_x, pos_y = conn.connect(nick_name, element)
player_id = str(player_id)
real_r = 0
SCALE = WINDOW_HEIGHT / map_height

while True:

    clock.tick(FPS)

    data = conn.send_and_get(pos_x, pos_y)
    players = data['players']
    players_list = []
    food = data['food']
    pos_x = players[player_id].ball.middle.x
    pos_y = players[player_id].ball.middle.y

    keyboard_control()
    mouse_control()
    """
    Wszystko ponizej obsługuje wyswietlanie gry
    """

    window.fill((255, 255, 255))

    # wyswietlanie jedzenia
    for f in food:
        x = f.middle.x * SCALE - pos_x * SCALE + WINDOW_WIDTH / 2
        y = f.middle.y * SCALE - pos_y * SCALE + WINDOW_HEIGHT / 2
        r = f.radius * SCALE
        pygame.draw.circle(window, (123, 100, 232), (int(x), int(y)), int(r))

    # wyswietlanie graczy
    for p in players:
        players_list.append(players[p])
        x = players[p].ball.middle.x * SCALE - pos_x * SCALE + WINDOW_WIDTH / 2
        y = players[p].ball.middle.y * SCALE - pos_y * SCALE + WINDOW_HEIGHT / 2
        # smoothly growing
        if p == player_id:
            real_r += (players[p].ball.radius - real_r) * 0.1
            players[p].ball.radius = real_r

        r = players[p].ball.radius * SCALE

        pygame.draw.circle(window, players[p].color, (int(x), int(y)), int(r))
        element = Element(window, x, y, r * 0.5, players[p].elem)
        element.display()
        # players[p].element
        # showing name
        font = pygame.font.SysFont("Consolas", int(r / 2))
        text = font.render(players[p].name, True, pygame.Color(0, 0, 0))
        window.blit(text, (x - (text.get_width()/2), y + r))

    SCALE = PLAYER_RADIUS / players[player_id].ball.radius

    # wyswietlanie rankingu
    players_list = sorted(players_list, key=lambda p: p.score)
    players_list.reverse()

    rank.display(players_list)

    # Crown display
    if len(players_list) > 0:
        best_player = players_list[0]
        x = best_player.ball.middle.x * SCALE - pos_x * SCALE + WINDOW_WIDTH / 2
        y = best_player.ball.middle.y * SCALE - pos_y * SCALE + WINDOW_HEIGHT / 2
        if best_player.id == player_id:
            best_player.ball.radius = real_r

        r = best_player.ball.radius * SCALE
        image = pygame.image.load("img/crown.png")
        image = pygame.transform.scale(image, (int(r * 2), int(r)))
        window.blit(image, (x - r , y - r - r/2))

    pygame.display.flip()

conn.disconnect()
