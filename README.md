# ImgToTxt

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ltlx4/ImgToTxt.git
$ cd ImgToTxt
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


## Tests

To run the tests, `cd` into the directory where `manage.py` is
And simply run.
```sh
(env)$ python manage.py test 
```
