# code is broken
from urllib2 import Request, urlopen, URLError
req = Request('https://docs.python.org/2/howto/urllib2.html')
try:
    response = urlopen(req)
    print(response.getstatus)
except URLError as e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
    else:
		print("what ever")
		# everything is fine