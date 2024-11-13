from concurrent import futures
import grpc
import greet_pb2
import greet_pb2_grpc
from grpc_reflection.v1alpha import reflection
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GreeterService(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        logger.info(f"Received request: {request.name}")
        return greet_pb2.HelloReply(message=f"Hello, {request.name}!")
    
    def SayHelloWorld(self, request, context):
        logger.info("Received request for 'Hello World' method")
        return greet_pb2.HelloReply(message="Hello World!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    
    SERVICE_NAMES = (
        greet_pb2.DESCRIPTOR.services_by_name['Greeter'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')
    server.start()
    logger.info("Server is running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
