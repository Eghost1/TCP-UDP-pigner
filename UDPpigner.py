# UDPPingerClient.py
from socket import *
import time

# Configurar la dirección y puerto del servidor
serverName = 'localhost'  # Cambia a la dirección IP del servidor si no se ejecuta localmente
serverPort = 12000

# Crear un socket UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Establecer tiempo de espera en un segundo
clientSocket.settimeout(1)

# Inicializar variables
sequence_number = 1
total_time = 0

# Enviar 10 pings al servidor
for i in range(1, 11):
    # Obtener el tiempo actual
    start_time = time.time()
    
    # Construir el mensaje de ping
    message = f'Ping {sequence_number} {start_time}'
    
    try:
        # Enviar el mensaje al servidor
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        
        # Esperar la respuesta del servidor
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        
        # Calcular el tiempo de ida y vuelta
        end_time = time.time()
        rtt = end_time - start_time
        total_time += rtt
        
        # Imprimir la respuesta del servidor y el tiempo de ida y vuelta
        print(f'Respuesta del servidor: {modifiedMessage.decode()}')
        print(f'Tiempo de ida y vuelta: {rtt} segundos\n')
    except timeout:
        # Imprimir 'Solicitud agotada' si no se recibe respuesta dentro de un segundo
        print('Solicitud agotada\n')
    
    # Incrementar el número de secuencia
    sequence_number += 1

# Imprimir el tiempo de ida y vuelta promedio
print(f'Tiempo de ida y vuelta promedio: {total_time / 10} segundos')

# Cerrar el socket
clientSocket.close()