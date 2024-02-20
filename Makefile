services:
	docker-compose -f ./devops/services/docker-compose.services.yml up -d

gitlab-ci-run-pytest:
	docker-compose -f ./devops/test/docker-compose.test.yml up