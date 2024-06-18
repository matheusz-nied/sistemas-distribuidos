import socket

# Teste Local
server_host = '127.0.0.1'
server_port = 15000

# Função para ler os dados enviado pelo cliente
def processar_dados(data):
    tokens = data.split()
    operation = tokens[0].lower()
    numbers = list(map(float, tokens[1:]))

    if operation == 'soma' or operation == '+':
        return sum(numbers)
    
    elif operation == 'subtrai' or operation == '-':
        print("entro no - ")
        if len(numbers) < 2:
            return "Erro: Necessário pelo menos dois números para subtrair."
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result
    
    elif operation == 'multiplica' or operation == '*':
        print("entro no * ")
        result = 1
        for num in numbers:
            result *= num
        return result
    
    elif operation == 'divide' or operation == '/':
        print("entro no / ")
        if len(numbers) < 2:
            return "Erro: Necessário pelo menos dois números para dividir."
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                return "Erro: Divisão por zero."
            result /= num
        return result
    
    else:
        return "Operação desconhecida."


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_host, server_port))

server_socket.listen(5)
print(f"Servidor ouvindo em {server_host}:{server_port}")

try:
    while True:
        print("Aguardando por uma conexão...")
        connection, client_address = server_socket.accept()

        try:
            print("Conexão de", client_address)

            while True:
                data = connection.recv(1024).decode('utf-8')
                if data:
                    print("Dados recebidos:", data)
                    result = processar_dados(data)
                    connection.sendall(str(result).encode('utf-8'))
                else:
                    print("Nenhum dado de", client_address)
                    break
        finally:
            connection.close()

except KeyboardInterrupt:
    print("Servidor interrompido pelo usuário")

finally:
    server_socket.close()