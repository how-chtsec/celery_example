from celery import Celery

# BROKER = 'amqp://username:password@IP/'
BROKER = 'amqp://guest@localhost//'

app = Celery('proj',
             broker=BROKER,
             backend='rpc://',
             include=['proj.tasks'])
app.conf.task_default_queue = 'worker'


app_checker = Celery('proj',
             broker=BROKER,
             backend='rpc://',
             include=['proj.checker'])
app_checker.conf.task_default_queue = 'checker'
