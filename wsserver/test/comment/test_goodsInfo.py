import httplib
import traceback

# cookie = 'u="123456789101"'
cookie = 'u="12345678910"'
base = 'localhost'
# base = 'n01.me-yun.com'
path = '/1.0/comment/goodsInfo?message_id=5a250de5ca71435b2394379a'
body = '{"c":"hello","to_id":"5a0157e0d2340121c7a0cfc8","c_type":"0"}'

try:
    header = {'Cookie': cookie, 'X-MeCloud-Debug': 1}
    print header
    httpClient = httplib.HTTPConnection(base, 8000, timeout=30)
    httpClient.request("GET", path,body, header)

    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    # print response.msg
    # print response.getheaders()
except Exception, e:
    print e
    msg = traceback.format_exc()
    print msg
finally:
    if httpClient:
        httpClient.close()
