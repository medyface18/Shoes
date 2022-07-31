# -*- coding: utf-8 -*-
import urllib.request
import time
http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
key = "cMJSBZTTKWpNT4yF3wKP-gkvngDccQt4"
secret = "gF8zk2-wzds5lpqhEcVd29-1qpSKjur_"
filepath = r"C:\Users\khadi\Downloads\images\coffeemug.jpg"
boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
fr=open(filepath,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename="co33.jpg"' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s--\r\n' % boundary)

http_body='\r\n'.join(str(data))
#print(http_body)
#buld http request
http_body=bytes(http_body,'utf-8')
req=urllib.request.Request(http_url)
#header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
if http_body is None:
    print( "Content is None!!")
else:
    print("hi") 
#req.getResponse()
req.data = http_body
try:
	#post data to server
	resp = urllib.request.urlopen(req)
	#get response
	qrcont=resp.read()
	print (qrcont)

except urllib.request.HTTPError as e:
    print (e.read())

print("hello")
