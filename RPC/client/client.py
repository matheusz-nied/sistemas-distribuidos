import xmlrpc.client

server_url = "http://localhost:8000"
proxy = xmlrpc.client.ServerProxy(server_url)

def show_menu():
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def get_numbers():
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    return x, y

while True:
    show_menu()
    choice = input("Digite a opção (1/2/3/4/5): ")

    if choice == '1':
        x, y = get_numbers()
        result = proxy.add(x, y)
        print(f"Resultado: {x} + {y} = {result}")
    elif choice == '2':
        x, y = get_numbers()
        result = proxy.subtract(x, y)
        print(f"Resultado: {x} - {y} = {result}")
    elif choice == '3':
        x, y = get_numbers()
        result = proxy.multiply(x, y)
        print(f"Resultado: {x} * {y} = {result}")
    elif choice == '4':
        x, y = get_numbers()
        result = proxy.divide(x, y)
        print(f"Resultado: {x} / {y} = {result}")
    elif choice == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida, escolha novamente.")

    print() 
