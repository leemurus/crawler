init:
	python3 manage.py makemigrations
	python3 manage.py migrate
	cp .env.copy .env