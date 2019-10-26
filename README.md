# ATLAN
## Technology Stack:
### Backend
* #### Django(Python3)
###### Django is used here because of it's powerful underlying code that makes it very convenient to use and focus on logic rather than boilerplate code and also because of Python's ease of use.
* #### Celery
###### It is used for executing background asynchronous queue based tasks.
* ####RabbitMQ
###### It is used as a message broker between application and celery.

## How to Use?
* Create a python3 virtual environment, navigate to project directory on terminal and install dependencies(listed in requirements.txt file) using the command
  `pip install requirements.txt` <br>
  RUN `python manage.py makemigrations` and `python manage.py migrate` <br>to create tables in database. <br>
  To run server, use command `python manage.py runserver`

* If Docker is installed, navigate to project directory on terminal,<br> RUN `docker-compose up`.

* Open a browser and navigate to <b>localhost:8000</b> to use the website.

## Security Features
* Cross site scripting (XSS) protection
* Cross site request forgery (CSRF) protection
* SQL injection protection

###### These security features are already provided by Django, so that makes a website safe from the most common vulnerabilities.

## Endpoints
###### start, pause, stop
###### All these three endpoints take a parameter as name, i.e name of the task.