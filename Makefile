services:
	docker-compose -f ./devops/services/docker-compose.services.yml up -d

gitlab-ci-run-pytest:
	docker-compose -f ./devops/test/docker-compose.test.yml up --exit-code-from wsgiapplication

dev_server:
	docker-compose -f ./devops/server/dev/docker-compose.dev-server.yml up