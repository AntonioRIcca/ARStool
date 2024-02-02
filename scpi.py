import socket


ip = '192.168.0.40'
port = 3490
addr = (ip, port)
is_connect = False
s = None

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 0)

    s.settimeout(2)
    s.connect(addr)
    is_connect = True
    print('Connesso!')
except socket.error:
    print('errore di connessione')


if is_connect:
    cmd = 'comando'
    try:
        s.sendto(cmd.encode() + b'\r\n', addr)
        print('Comnando inviato correttamente')
    except socket.error:
        print('Comnando non inviato')

    var = s.recv(4096).decode('utf-8')[:-1]
    print('Risposta: ', var)
