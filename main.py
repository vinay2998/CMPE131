from socket import *
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
emailFrom = "vinay.car@gmail.com"
emailTo  = "vinayan.kathiresan@sjsu.edu"
# Choose a mail server (e.g. Google mail server) and call it mailserver
#mailserver =  ("smtp.gmx.com", 25)
#mailserver = ('localhost', 1025)
mailserver = ("smtp.gmail.com",587)

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
#clientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)
clientSocket.connect(mailserver)
# Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received.')

# Send MAIL FROM command and print server response.
# Fill in start
fromCommand = 'Mail from ' + emailFrom + '\r\n'
clientSocket.send(fromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptCommand = 'Rcpt To ' + emailTo + '\r\n'
clientSocket.send(rcptCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = 'Data\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
# Fill in end

# Send message data.
# Fill in start
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = 'Quit\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
# Fill in end

print("Code finished")