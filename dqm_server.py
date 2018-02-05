import os
import sys
sys.path.append('../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{appname}.settings".format(appname=os.environ['DJANGO_APP']))
import django
django.setup()
import time
from django_queue_manager import worker_manager
from django_queue_manager.models import DQMQueue
from django_queue_manager.server_manager import TaskSocketServerThread
worker_manager.start()
server_thread = TaskSocketServerThread('127.0.0.1', 8000)
time.sleep(5)
socket_server = server_thread.socket_server()
socket_server.serve_forever()
