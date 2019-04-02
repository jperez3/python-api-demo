build: 
	docker build . -t joeperez/docker-python-api:latest

run:
	docker run --name python_api -d -p 5000:5000 joeperez/docker-python-api:latest

up:
	make build run

stop:
	docker stop python_api

remove:
	docker rm python_api && docker rmi joeperez/docker-python-api:latest

destroy:
	make stop remove