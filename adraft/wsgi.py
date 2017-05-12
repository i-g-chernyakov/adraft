import os
import sys

from django.core.wsgi import get_wsgi_application


path = '/home/kamen/adraft'
if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "adraft.settings.local"
os.environ['ADRAFT_DATABASE_ENGINE'] = 'django.db.backends.postgresql_psycopg2'
os.environ['ADRAFT_DATABASE_NAME'] = 'adraft'
os.environ['ADRAFT_DATABASE_USER'] = 'adraft'
os.environ['ADRAFT_DATABASE_PASSWORD'] = '123456'
os.environ['ADRAFT_DATABASE_HOST'] = '127.0.0.1'
os.environ['ADRAFT_DATABASE_PORT'] = '5432'
os.environ['ADRAFT_SECRET_KEY'] = '(l3-jtu8c_5$=sgh+9zme1^t-^mbq6nsi+s4x7r6esvxhyeo3v'

application = get_wsgi_application()
