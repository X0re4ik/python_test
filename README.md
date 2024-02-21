
# ОС (Ubuntu 20.04)
## Стартуем
1. Подготовка ОС
```sh
$ sudo apt update
$ sudo apt install git docker docker-compose make
```
2. Клонирование репозитория с github:
```sh
$ git clone https://github.com/X0re4ik/python_test.git
$ mv python_test/ backend/ 
$ cd backend/
```

## Для разработчиков
1. Создание виртуального окружения
```sh
$ python3.10 -m venv .venv
$ source .venv/bin/activate
```
2. Создание .env файла (образец взять из `./src/.example.env` или `./devops/services/.docker.services.env`)
```sh
$ cp ./src/.example.env ./src/.env
$ nano ./src/.env
```
3. Загрузка внешних приложений (Redis, PostgreSQL, pgAdmin)
```sh
$ make services
```
4. Проверяем, что все работает корректно
```sh
$ cd src
$ make test
```

## Для DevOps
1. Запуск автотестов в отдельном docker контейнере
```sh
$ make gitlab-ci-run-pytest
```
2. Запуск сервера в отдельном docker контейнере
```sh
$ make server_dev_version
```



# Общий отчет
Из дополнительных выполнил 3 из 4:
- [+] есть автодокументация API
- [-] есть система логирования
- [+] сервис завёрнут в docker контейнер
- [+] наличие юнит тестов

Использовал Django REST framework, для неблокирующих задач использовал Celery, 
тестирование производил при помощи pytest и всевозможных модулей (mixer, mock).

Выполнил Мочалов Антон Вячеславович. 
Коллеги, прошу уважать чужое время и силы, ожидаю от вас подробную обратную свзязь, даже самую негативную.

PS. Последняя фраза без негатива, встречаются компании, которые игнорируют задания и остается осадочек