#!/bin/bash
source /home/serg/workbox/env/bin/activate
exec gunicorn -c "/home/serg/workbox/workbox/gunicorn_config.py" workbox.wsgi 