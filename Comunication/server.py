import socket
import zipfile
import os


def compactar_diretorio(diretorio, arquivo_saida):
    with zipfile.ZipFile(arquivo_saida, 'w') as zipf:
        for raiz, _, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                caminho_completo = os.path.join(raiz, arquivo)
                relativo = os.path.relpath(caminho_completo, diretorio)
                zipf.write(caminho_completo, relativo)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.1.16', 8080))
server.listen(1)

connection, address = server.accept()

# Recebe o nome do diretório a ser compactado
diretorio_cliente = connection.recv(1024).decode()

# Nome do arquivo ZIP de saída
arquivo_zip_saida = 'arquivo_enviado.zip'

# Compacta o diretório do cliente
compactar_diretorio(diretorio_cliente, arquivo_zip_saida)

# Envia o arquivo ZIP
with open(arquivo_zip_saida, 'rb') as file:
    connection.sendfile(file)

print('Arquivo ZIP enviado.')

server.close()
