import socket
print("Solving 100 math problem's.")
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(('challenge.ctf.games', 32114))
print(connection.recv(1024).decode())
connection.send(b'y')
print(connection.recv(1024).decode())
count=0
while count<100:
    count+=1
    question = connection.recv(1024).decode()
    question = question.split()
    num1 = question[2]
    num2 = question[4][:-1]
    operation = question[3]
    ans = eval(f'{num1}{operation}{num2}')
    if '.' in num1 or '.' in num2:
        ans=round(ans, 1)
        connection.send(str(ans).encode())
    else:
        ans = int(ans)
        connection.send(str(ans).encode())
    result = connection.recv(1024).decode()
    print(result, end='')
result = connection.recv(1024).decode()
print(result, end='')
