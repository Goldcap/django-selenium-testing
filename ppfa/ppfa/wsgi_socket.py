import os
import gevent.socket
import redis.connection

redis.connection.socket = gevent.socket
os.environ.update(DJANGO_SETTINGS_MODULE='ppfa.settings')
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer

print "HELLO"

application = uWSGIWebsocketServer()
