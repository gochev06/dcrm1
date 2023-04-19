# Django CRM

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/gochev06/dcrm1
$ cd dcrm1
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ venv --no-site-packages env
$ source env/Scripts/activate
```

Then install the dependencies:

```sh
Install MySQL on the computer
(env)$ pip install mysql
(env)$ pip install mysql-connector
(env)$ pip install mysql-connector-pytho
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://localhost:8000/`.
