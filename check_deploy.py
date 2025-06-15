import os
import sys

wsgi_path = os.getenv("WSGI_PATH")

exec(open(wsgi_path).read())

from django.core.management import call_command
call_command("check", "--deploy")