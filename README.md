# dj-ratelimit-example
Example ratelimit project

dj-ratelimit repository: https://github.com/conorbergman/py-ratelimit
dj-ratelimit pypi: https://pypi.org/project/dj-ratelimit/

Install dj-ratelimit with pip: `pip install dj-ratelimit`

To run install django and py-ratelimit. Verify installation works by running `python manage.py runserver` and go to `http://127.0.0.1:8000/myapp`.

To test ratelimit setup postman (or use curl if preferred) to make a GET request to `http://127.0.0.1:8000/myapp/`. 
By default this example application has a burst limit of 2 requests/minute and a ratelimit of 1 request/minute.
Make 3 requests, you'll see the first two return 'Hello World' 200 responses, but the 3rd is a ratelimited 429
response.
