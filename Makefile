API_SERVER=api-server
API_DB=api-db
WEB_SERVER=web-server

run:
	docker-compose build
	docker-compose up -d

stop:
	docker stop ${API_SERVER} ${API_DB} ${WEB_SERVER}
	docker rm ${API_SERVER} ${API_DB} ${WEB_SERVER}
