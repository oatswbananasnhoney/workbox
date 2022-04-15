#!/bin/bash
source /home/serg/workbox/web/env/bin/activate
exec gunicorn -c "/home/serg/workbox/web/gunicorn_config.py" workbox.wsgi 