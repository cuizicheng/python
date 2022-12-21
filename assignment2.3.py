import requests
import urllib2
import urllib
#pip install
URL = 'http://c.biancheng.net/uploads/course/python_spider/191009.html'
res.encoding = 'utf-8'
res = requests.get(URL)
print(type(res))
print(res.text)
res = requests.put(URL)
print(type(res))
print(res.text)
