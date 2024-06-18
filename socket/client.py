import socket

server_host = '127.0.0.1'  # endereço IP criado pelo servidor
server_port = 15000


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_host, server_port))
    
    while True:
        print("Calculadora Distribuída")
        print("Digite a operação seguida dos números separados por espaço (exemplo 1: soma 1 2 3 4) (exemplo 2: + 5 6 7 8)")
        user_input = input("Operação: ")
        
        client_socket.sendall(user_input.encode('utf-8'))
        
        response = client_socket.recv(1024)
        print("Resultado:", response.decode('utf-8'))
        
        if input("Deseja realizar outra operação? (s/n): ") == 'n':
            break
except Exception as e:
    print("Erro na conexão: ", e)
finally:
    client_socket.close()