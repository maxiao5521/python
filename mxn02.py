import urllib.request
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
proxy_handle = ({'http':'http://183.51.190.51:33913'},{'http':'http://117.184.67.118:8060'},{'http':'http://210.5.10.87:53281'})
for proxy_handle in proxy_handle:
    try:
        opener = urllib.request.build_opener(proxy_handle)
        reponse = opener.open('http://www.baidu.com')
        if response.status==200:
            print('请求成功')
        else:
            print('url错误') 
    except:
        print('代理失效')