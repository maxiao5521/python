import urllib.parse
import urllib.response
data- urllib. parse, urlencode(('wd':'hello'))
print(data)
url='http: //www.baidu.com/s?'+data
response = urllib. request.urlopen(ur1)
HTML=response.read().decode('utf8)
print(HTML)

data = bytes(urllib.parse.urlencode({'pw':'777','un':'888'}),enconding='utf8')
url = 'http://httpbin.org/post'
response = urllib.request.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result)