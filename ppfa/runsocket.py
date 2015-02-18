#!/bin/bash

uwsgi --virtualenv /var/venvs/ppfa --http-socket /var/run/nginx/ws.socket --gevent 1000 --http-websockets --workers=2 --master --module ppfa.wsgi_socket&

exit 0
