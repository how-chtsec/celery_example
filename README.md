### Celery example code
Celery example code for brute-force attack.

### Enviroment
Install rabbitmq-server, python3

Install python lib:
``` bash
pip install -r requirements.txt
```

Change the ```BROKER``` in ```proj/celery.py```to your rabbitmq server



Change the ```url``` value in test.py


### Usage
Run worker
``` bash
celery -A proj.tasks worker -l INFO -Q worker

// Windows
celery -A proj.tasks worker -l INFO -Q worker -P eventlet
```


Run checker
``` bash
celery -A proj.checker worker -l INFO

// Windows
celery -A proj.checker worker -l INFO -P eventlet
```

Run test
``` bash
python3 test.py
```