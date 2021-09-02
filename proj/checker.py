from .celery import app_checker

@app_checker.task(queue='check')
def check_iotgoat_default_creds(resp):
    if 'Location' in resp['headers']:
        if resp['status_code'] == 302 and resp['headers']['Location'] == '/cgi-bin/luci/' and resp['len_text'] == 0:
            return '%s %s / %s' % (resp['url'], resp['data']['luci_username'], resp['data']['luci_password'])
        else:
            return False