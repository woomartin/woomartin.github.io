from urllib.request import urlopen
url = 'https://api.bilibili.com/x/player/pagelist?bvid=BV1tp4y1i7rL&jsonp=jsonp'
#返回http.client.HTTPResponse object at 0x00000235BA25A160
print(urlopen(url))

#返回get到的页面的源代码
print(urlopen(url).read())
# decode是将base类型转为encoding 指定的编码格式解码字符串，不指定则转为默认编码，如utf-8