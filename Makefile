install-tools:
	brew install grpcurl make python
install:
	pip install -r requirements.txt
generate:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. greet.proto
start:
	python server.py
list:
	grpcurl -plaintext localhost:50051 list
test:
	grpcurl -plaintext -d '{"name": "John"}' localhost:50051 greet.Greeter/SayHello