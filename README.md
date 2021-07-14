# stack-django


## Requirements
  * Python-version -: Python 3.8.5
  * Django-version -: 3.1.7

### After installing requirements cross check it using:
```sh
$ python3 -V
$ django-admin --version
```
## Setup

The first thing to do is to clone the repository:
```sh
$ https://github.com/prijittech/digital_album.git
$ git checkout master
$ cd stack-django
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ sudo apt install python3-venv
$ python3 -m venv env
$ source env/bin/activate
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Once `pip` has finished downloading the dependencies:

## DataBase configrations
After DB configurations

```sh
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`


 

