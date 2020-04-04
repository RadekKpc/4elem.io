import socket
import pickle

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
        print(data_rec)
        self.id = (data['id'])
        print("Przydzielono id: ",self.id)

    def disconnect(self):
        self.connection.close()


conn = Client()
conn.connect("Radek","fire")
conn.disconnect()