import socket
import threading
import random
import pickle
from Player import Player
from Point import Point
from Map import Map
from Ball import Ball
import math

# connection setting
HOST = '127.0.0.1'
PORT = 22000

# Game settings
START_RADIUS = 10
COUNT_OF_FOOD = 100
FOOD_RADIUS = 20
MAP_WIDTH = 1000
MAP_HEIGHT = 1000

count_of_playesrs = 0
players = {}
food = []
id_for_next_player = 1000
game_map = Map(MAP_WIDTH,MAP_HEIGHT)
# functions

def random_ball(radius):
    random_ball = Ball(Point(-1,-1),radius)
    while True:
        x = random.randint(game_map.lower_left.x,game_map.upper_right.x)
        y = random.randint(game_map.lower_left.y,game_map.upper_right.y)
        random_ball.middle.x = x
        random_ball.middle.y = y
        for p in players:
            if players[p].ball == random_ball:
                continue
        return random_ball

def player_thread_service(conn,add,player_id):
    global food,players

    # receive name and elem from client
    data = conn.recv(64)
    start_data = pickle.loads(data)

    name = start_data['name']
    elem = start_data['elem']

    # creating the player and set him in players set
    str_id = str(player_id)
    player_ball = random_ball(START_RADIUS)
    player = Player(player_ball,player_id,name,elem)
    players[str_id] = player

    # sending id (pozniej moze ustawienia mapy lub cos zoabczymy)
    conn.send(pickle.dumps({'id': player_id}))

def rand_food():
    global game_map
    while True:
        x = random.randint(game_map.lower_left.x,game_map.upper_right.x)
        y = random.randint(game_map.lower_left.y,game_map.upper_right.y)
        if (x,y) not in food:
            return(x,y)

def start_new_game():
    global food,random_ball
    for _ in range(COUNT_OF_FOOD):
        food.append(random_ball(FOOD_RADIUS))
    print(food)




s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.bind((HOST,PORT))
    s.listen()
except socket.error as e:
    print(str(e))
    quit()


print("Starting new game...")
start_new_game()
print("Listen on "+str(HOST)+":"+str(PORT)+" ...")

while True:

    try:
        conn, add = s.accept()
        print("New connection with:",add)
    except socket.error as e:
        print(e)
        quit()
    id_for_next_player += 1
    count_of_playesrs += 1
    threading.Thread(target=player_thread_service,kwargs={'conn' : conn,'add' : add,'player_id': id_for_next_player}).start()


print("Server exit")

