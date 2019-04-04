default:
	make up

build: 
	docker build . -t joeperez/python-app:latest

run:
	docker run --name python_container -d -p 5000:5000 joeperez/python-app:latest

up:
	make build run

stop:
	docker stop python_container

remove:
	docker rm python_container && docker rmi joeperez/python-app:latest

destroy:
	make stop remove

debug:
	docker exec -it python_container /bin/ash	