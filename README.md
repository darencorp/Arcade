## Requirements
* Ubuntu 15.04
* [Pyhton 3.4.2](https://www.python.org/download/releases/3.4.2/)
* virtualenv
* nginx

## Install
- clone project
- sudo apt install nginx
- put file 'default' to /env/nginx/sites-available
- sudo nginx -s reload
- cd to project catalog and run: virtualenv env
- env/bin/pip3 install -r requirements.txt
- env/bin/uwsgi --ini uwsgi.ini
- open in browser localhost
