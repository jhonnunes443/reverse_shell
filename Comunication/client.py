import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.1.16', 7272))
print('Connected [!]\n')

namefile = str(input('Arquivo> '))

client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

print(f'{namefile} file received [ok]')

client.close()
