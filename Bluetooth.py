from bluetooth import *


bufferIn = []
bufferOut = []
running = True
def onReceiveAudio(audio):
    #puts audio in the bufferOut
    return

def sendAudio():
    #sends audio from buffer to phone
    return

def onReceiveText(text):
    #receive text from phone and puts it in bufferIn
    print("received [%s]" % text)
    bufferIn.append(text)
    return

def sendText():
    #sends text from the bufferIn to display
    return


server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("", PORT_ANY)) #bind to any available port
server_sock.listen(1) #Listen for connections

port = server_sock.getsockname()[1] #Get Port

uuid = "b8162268-3e67-4749-9508-cb30b86703c7"

advertise_service(server_sock, "PhonixServer",
                  service_id=uuid,
                  service_classes=[uuid, SERIAL_PORT_CLASS],
                  profiles=[SERIAL_PORT_PROFILE],
                  #                   protocols = [ OBEX_UUID ]
                  )

connected = True
while running:
    while ~connected:
        print("Waiting for connection on RFCOMM channel %d" % port)
        client_sock, client_info = server_sock.accept()
        print("Accepted connection from ", client_info)
        connected = True
        try:
            while connected:
                data = client_sock.recv(1024)
                if len(data) != 0:
                    onReceiveText(data)
                else:
                    connected = False
        except IOError:
            connected = False

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")