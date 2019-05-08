from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

decode_key = unquote('키 입력')

url = 'URL주소'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : decode_key, quote_plus('pageNo') : '1', quote_plus('numOfRows') : '2', quote_plus('title') : '1987', quote_plus('rtNo') : '2017-MF02149', quote_plus('aplcName') : '주식회사 우정필름' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)

