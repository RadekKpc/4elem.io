import socket
import pickle
import time
# connection setting
HOST = '127.0.0.1'
PORT = 22000


class Client:

    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.id = -1

    def connect(self,name,elem):
        self.connection.connect((HOST,PORT))
        """
        After connection we need:
        1. send name and element type
        2. get our id
        """

        # 1 sending basic data
        self.connection.send(pickle.dumps({'name': name,'elem': elem}))

        # 2 receiving data from server
        # Here we have id only, but in the further this may be map setting
        # or another significant infromations
        data_rec =  self.connection.recv(128)
        data = pickle.loads(data_rec)
        print(data)
        self.id = (data['id'])
        return (data['width'],data['height'],data['id'],data['x'],data['y'])

    def disconnect(self):
        self.connection.close()

    def send_and_get(self,x,y):
        try:
            data = {'x' : x,'y': y}
            data = pickle.dumps(data)
            self.connection.send(data)

            # Ładuje słownik pod 'food' mamy liste jedzenia klasa Ball
            # Pod 'players' mamy slownik graczy klasa Players
            data_rec = self.connection.recv(1024*8)
            data_rec = pickle.loads(data_rec)

        except Exception as e:
            print(e)

        return data_rec
