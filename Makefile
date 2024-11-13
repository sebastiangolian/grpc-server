install-tools:
	brew install grpcurl make python protobuf
install:
	pip install -r requirements.txt
generate:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. greet.proto
generate-pb:
	protoc --descriptor_set_out=greet.pb greet.proto
start:
	python server.py
listen-port:
	lsof -i :50051
list:
	grpcurl -plaintext 127.0.0.1:50051 list
test:
	grpcurl -plaintext 127.0.0.1:50051 greet.Greeter/SayHelloWorld
test1:
	grpcurl -plaintext -d '{"name": "John"}' 127.0.0.1:50051 greet.Greeter/SayHello
	