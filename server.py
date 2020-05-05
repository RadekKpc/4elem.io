import socket
import threading
import pickle
from map_components.map import Map

# connection setting
HOST = '127.0.0.1'
PORT = 22000

MAP_WIDTH = 1000
MAP_HEIGHT = 1000

game_map = Map(MAP_WIDTH, MAP_HEIGHT)


def player_thread_service(conn, add, player_id):
    # receive name and elem from client
    data = conn.recv(64)
    start_data = pickle.loads(data)

    name = start_data['name']
    elem = start_data['elem']

    # creating the player and set him in players set
    x, y = game_map.create_new_player(player_id, name, elem)

    # sending id (pozniej moze ustawienia mapy lub cos zoabczymy)
    conn.send(pickle.dumps({'id': player_id,
                            'width': MAP_WIDTH,
                            'height': MAP_HEIGHT,
                            'x': x,
                            'y': y}))

    # petla obsługująca rządania klienta

    while True:
        try:

            # Uaktualnienie pozycji
            data = conn.recv(32)

            if not data:
                break
            data = pickle.loads(data)

            game_map.update_player(player_id, data['x'], data['y'])
            # Sprawdzanie kolizji, zwiekszanie score i promienia

            # Zjadanie innych graczy i jedzenia
            game_map.eating()

            # wyslanie danych o graczach i jedzeniu
            receiv_data = pickle.dumps({'players': game_map.get_players(), 'food': game_map.get_food()})
            conn.send(receiv_data)

        except Exception as e:
            print("Error2: ", e)
            break

    conn.close()


# PROGRAM

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
    s.listen()
except socket.error as e:
    print("Error", (str(e)))
    quit()

print("Starting new game...")
game_map.start_new_game()
print("Listen on " + str(HOST) + ":" + str(PORT) + " ...")

while True:

    try:
        conn, add = s.accept()
        print("New connection with:", add)
    except socket.error as e:
        print("Error", (str(e)))
        quit()
    id_for_next_player = game_map.get_id_for_next_player()
    threading.Thread(target=player_thread_service,
                     kwargs={'conn': conn, 'add': add, 'player_id': id_for_next_player}).start()

print("Server exit")
