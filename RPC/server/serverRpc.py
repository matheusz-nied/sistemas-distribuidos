from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from calculator import CalculatorAPI

def run_server():
    server = SimpleXMLRPCServer(("localhost", 8000))
    server.register_instance(CalculatorAPI())
    print("Servidor RPC iniciado. Aguardando conexões...")
    server.serve_forever()

if __name__ == "__main__":
    run_server()