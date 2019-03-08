# Log My HTTP Requests

## Overview 
This project is a simple http webserver that logs every requests with 200 Status code and help you to get full detail of request for diagnostic usage or whatever. 

## How to Run ?

```
#clone project 
pip install virtualenv
virtualenv venv
. venv/bin/activate
export FLASK_DEBUG=1
export FLASK_APP=app.py

flask run --host=0.0.0.0 --port=8080
```
## How to use ?
Easily just put the url of server in your other applications to redirect the requests here to see what is happening.
