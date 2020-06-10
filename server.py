import socket
import threading
import pickle
from map_components.map import Map

# connection setting
HOST = '127.0.0.1'
PORT = 22000
BACKLOG = 30
MAP_WIDTH = 1000
MAP_HEIGHT = 1000

game_map = Map(MAP_WIDTH, MAP_HEIGHT)


def player_thread_service(connection, player_id):
    # receive name and elem from client
    data = connection.recv(64)
    start_data = pickle.loads(data)

    name = start_data['name']
    elem = start_data['elem']

    # creating the player and set him in players set
    x, y = game_map.create_new_player(player_id, name, elem)

    # sending id (pozniej moze ustawienia mapy lub cos zoabczymy)
    connection.send(pickle.dumps({'id': player_id,
                                  'width': MAP_WIDTH,
                                  'height': MAP_HEIGHT,
                                  'x': x,
                                  'y': y}))

    # petla obsługująca rządania klienta

    while True:
        try:

            # Uaktualnienie pozycji
            data = connection.recv(64)
            if not data:
                break
            data = pickle.loads(data)

            game_map.update_player(player_id, data['x'], data['y'])
            # Sprawdzanie kolizji, zwiekszanie score i promienia

            # Zjadanie innych graczy i jedzenia
            game_map.eating()

            # wyslanie danych o graczach i jedzeniu
            receiv_data = pickle.dumps({'players': game_map.get_players(), 'food': game_map.get_food()})
            msg_length = len(receiv_data)
            msg_l = pickle.dumps(msg_length)
            connection.send(msg_l)
            connection.send(receiv_data)

            game_map.game_end_check()

        except Exception as ex:
            print("Error2: ", ex)
            break

    connection.close()


# PROGRAM

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((HOST, PORT))
        s.listen(BACKLOG)
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
            id_for_next_player = game_map.get_id_for_next_player()
            threading.Thread(target=player_thread_service,
                             kwargs={'connection': conn, 'player_id': id_for_next_player}).start()
        except socket.error as e:
            print("Error", (str(e)))
            quit()
