flake8:
	flake8 .

isort:
	isort .

requirements:
	pip install -r requirements.txt

freeze:
	pip freeze -l > requirements.txt


test:
	pytest -s -v


migrations:
	python manage.py makemigrations
	
migrate:
	python manage.py migrate

del_migration_files:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && \
	find . -path "*/migrations/*.pyc"  -delete

dev_server:
	make migrate && \
	python manage.py runserver