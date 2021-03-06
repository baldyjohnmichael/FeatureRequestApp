# Feature Request App

## How to run locally

### Requirements
**OS**: Ubuntu
**Python**: 3.4 or greater
**pip**: pip 8.1.1 or greater

### Setting up the Enviroment
1. fork and clone the repo onto your local machine.
```
$ git clone https://github.com/baldyjohnmichael/FeatureRequestApp
```
2. Check to see you have the correct version of python installed.
```
$ python3
```
if early than python 3.4, download and install a proper version.
3. Create a virtual enviroment named venv, in the console type
```
$ python3 -m venv venv
```
4. activate the virtual enviroment with
```
$ source venv/bin/activate
```
5. install Flask
```
$ pip install flask
```
6. check to see if Flask was properly installed
```
$ python3
>>> import flask
```
if 'import flask' does not return an error, then Flask has been properly installed.

7. set the enviroment variable FLASK_APP to featApp.py
```
$ export FLASK_APP=featApp.py
```
8. run the app
```
$ flask run
```
this command should return

```
* Serving Flask app "featApp"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
9. in your prefered web browser, go to the url http://localhost:5000/ or http://localhost:5000/index
