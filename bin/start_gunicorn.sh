#!/bin/bash
source /home/serg/workbox/web/env/bin/activate
exec gunicorn -c "/home/serg/workbox/workbox/gunicorn_config.py" workbox.wsgi 