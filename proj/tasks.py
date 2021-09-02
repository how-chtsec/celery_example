import requests
import urllib3
from .celery import app
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@app.task
def post_data(url, data):
    r = requests.post(url, data=data, allow_redirects=False, verify=False)
    resp = {'url': url,
            'status_code': r.status_code,
            'len_text': len(r.text),
            'headers': dict(r.headers),
            'data': data}
    return resp
