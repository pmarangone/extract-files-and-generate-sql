deploy:
	gunicorn -w 4 -b 0.0.0.0:8000 app:app
run:
	flask --app app run	
debug:
	flask --app app run --debug