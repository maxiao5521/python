import requests
URLS = []
url = 'http://www.4399dmw.com/haizeiwang/tupian/'
response = requests.get(url)
HTML = response.text
lines = HTML.split('\n')
for line in lines:
    if'<img'in line:
        split_ = line.split('<img src=')
        for i in split_:
            if 'http' in i or 'https' in i:
                url = i.split('"')[1]
                if 'jpg' in url:
                    URLS.append(url)
for url in URLS:
    response = requests.get(url)
    content = response.content
    name = url.split('/')[-1]
    with open(name,'wb') as f:
        f.write(content)
    