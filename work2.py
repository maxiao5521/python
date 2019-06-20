import urllib.request
response = urllib.request.urlopen('https://www.17k.com/chapter/2933095/36699279.html')
print(response.read().decode('utf8'))
print(response.status)
print(response.getheader('Content-Type'))  
    