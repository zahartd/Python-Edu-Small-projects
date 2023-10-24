import socket
HOST = "localhost"
PORT = 9999
print("Клиент игры 'Виселица' приветствует вас!")
print("Подключение к серверу {}:{}" .format(HOST, PORT))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.sendall(bytes("START", "utf-8"))
data = sock.recv(1024).decode()
data = data.split(";")
if data[0] == "GUESS":
    print("Угадайте число от {} до {}. У вас 10 попыток." .format(data[1], data[2]))
    while True:
       x = input("Ваш ответ: ")
       if x == "q":
           sock.sendall(bytes("GOODBYE", "utf-8"))
           break
       sock.sendall(bytes("TRY;{}" .format(x), "utf-8"))
       data = sock.recv(1024).decode()
       data = data.split(";")
       if data[0] == "TRUE":
           print("Ура, вы угадали!!!")
           break
       elif data[0] == "FALSE":
           print("Вы не правы. У вас есть еще попытки ...")
           if data[1] == "TRY_MORE":
               print("Загаданное число больше, чем введеное вами.")
           elif data[1] == "TRY_LESS":
               print("Загаданное число меньше, чем введеное вами.")
       elif data[0] == "FAIL":
           print("Вы не угадали!!! :(")
           break
sock.sendall(bytes("GOODBYE", "utf-8"))
sock.close()