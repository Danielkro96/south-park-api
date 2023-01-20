# Start the Guncorn WSGI server.
gunicorn --bind 0.0.0.0:8080 run:app
