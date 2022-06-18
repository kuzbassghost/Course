import  socket

SERVER_ADRESS = ('localhost', 15253)

client = socket.socket()
client.connect(SERVER_ADRESS)
client.send(bytes("Hello", encoding="UTF-8"))
data = client.recv(4096)
print(data.decode("UTF-8"))