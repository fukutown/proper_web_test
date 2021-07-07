API_SERVER=api-server
API_DB=api-db
WEB_SERVER=web-server

run:
	docker-compose -f docker-compose.yaml -f development.yaml up -d --build

stop:
	docker-compose down
