

me = 'college'
bind = '0.0.0.0:8000'
#bind = 'unix:/home/illace-web/diceapp-backend/diceapp.sock'
workers = 2
worker_class = 'gevent'
max_requests = 1000
user = 'root'
group = 'root'
reload = True
accesslog = '-'
logfile = 'access.log'
errorlog = 'error.log'
#group = 'nginx'
secure_scheme_headers = {
    'X-FORWARDED-PROTOCOL': 'ssl',
    'X-FORWARDED-PROTO': 'https',
    'X-FORWARDED-SSL': 'on'
   }
loglevel = 'debug'

