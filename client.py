import socket
import pickle


# connection setting

class Client:

    def __init__(self, ip, port):
        self.host = ip
        self.port = port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.id = -1

    def connect(self, name, elem):
        self.connection.connect((self.host, self.port))
        """
        After connection we need:
        1. send name and element type
        2. get our id
        """

        # 1 sending basic data
        self.connection.send(pickle.dumps({'name': name, 'elem': elem}))

        # 2 receiving data from server
        # Here we have id only, but in the further this may be map setting
        # or another significant infromations
        data_rec = self.connection.recv(128)
        data = pickle.loads(data_rec)
        print(data)
        self.id = (data['id'])
        return (data['width'], data['height'], data['id'], data['x'], data['y'])

    def disconnect(self):
        self.connection.close()

    def send_and_get(self, x, y):
        data_rec = ""
        try:
            data = {'x': x, 'y': y}
            data = pickle.dumps(data)
            self.connection.send(data)

            # Ładuje słownik pod 'food' mamy liste jedzenia klasa Ball
            # Pod 'players' mamy slownik graczy klasa Players
            length = self.connection.recv(6)
            length = pickle.loads(length)
            data = b''
            while True:
                packet = self.connection.recv(4096)
                data += packet
                if len(data) >= length:
                    break
            data_rec = pickle.loads(data)
        except Exception as e:
            print(e)

        return data_rec
