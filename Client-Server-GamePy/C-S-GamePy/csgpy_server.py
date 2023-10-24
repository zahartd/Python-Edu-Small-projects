import random
import socketserver
HOST = "localhost"
PORT = 9999
class GibbetHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).decode()
        print("Клиент {} сообщает: {}" .format(self.client_address[0], self.data))
        x = random.randint(1, 100)
        print("Загаданное число:", x)
        if self.data == "START":
            self.request.sendall(bytes("GUESS;1;100", "utf-8"))
            try_count = 10
            while True:
                self.data = self.request.recv(1024).decode()
                data = self.data.split(";")
                if data[0] == "TRY":
                    print("Клиент {} сообщает: {}" .format(self.client_address[0], self.data))
                    if int(data[1]) == x:
                        self.request.sendall(bytes("TRUE", "utf-8"))
                        print("Клиент {} выйграл!!!" .format(self.client_address[0]))
                        break
                    else:
                        try_count -= 1
                        if try_count == 0:
                            self.request.sendall(bytes("FAIL", "utf-8"))
                            break
                        elif int(data[1]) < x:
                            self.request.sendall(bytes("FALSE;TRY_MORE", "utf-8"))
                        elif int(data[1]) > x:
                            self.request.sendall(bytes("FALSE;TRY_LESS", "utf-8"))
                elif data[0] == "GOODBYE":
                    print("Клиент убег.....")
server = socketserver.TCPServer((HOST, PORT), GibbetHandler)
print("Сервер игры 'Виселеца' запущен!")
server.serve_forever()