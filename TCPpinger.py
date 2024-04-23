from socket import *
import time

servidor = 'localhost' 
puerto = 12000

#creamos el socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((servidor,puerto))


#settimeout me permite poner un tiempo de espera (como un limite) 
clientSocket.settimeout(1)

secuencia = 1
tiempo_total = 0
cont = 0

while cont<10:
    #guardamos el tiempo actual (de comienzo) del envio del ping
    tiempo_comienzo = time.time()
    
    msg = 'Ping ' + str(secuencia) + ' ' + str(tiempo_comienzo)
    #print(message)
    
    try:
        #enviamos datos a traves edl socket udp
        clientSocket.send(msg.encode())

        respuesta = socketCliente.recv(1024).decode()
        
        tiempo_final = time.time()
        #restando el tiempo guardado al inicio, con el tiempo q acabamos de guardar, para obtener RTT
        rtt = tiempo_final - tiempo_comienzo
        tiempo_total += rtt
        
        print('Respuesta del servidor:', respuesta)
        #rtt
        print('Tiempo de ida y vuelta: '+str(rtt)+ 'segundos\n')
    except timeout:
        #en caso de no recibir en 1 segundo, imprimos solicitud agotada
        print('Solicitud agotada\n')
    
    secuencia += 1
    cont += 1

#rtt prom
print('Tiempo de ida y vuelta promedio: '+str(tiempo_total/10)+'segundos')

clientSocket.close()
