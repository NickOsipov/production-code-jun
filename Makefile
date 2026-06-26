build:
	docker build -t flask-app .

run:
	docker run -p 5000:5000 --name flask-app flask-app