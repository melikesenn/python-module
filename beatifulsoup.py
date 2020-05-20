
html_doc = """
<html>
<head>
<title>
The Dormouse's story
</title>
</head>
<body>
<p class="title">
<b>
The Dormouse's story
</b>
</p>
<p class="story">
Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1">
Elsie
</a>
,
 <a class="sister" href="http://example.com/lacie" id="link2">
 Lacie
 </a>
 and
  <a class="sister" href="http://example.com/tillie" id="link3">
  Tillie
 </a>
 and they lived at the bottom of a well.
  </p>
<p class="story">
   ...
 </p>
 <div> 48415415 </div>
  </body>
 </html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
result = soup.prettify() #etiketleri düzeltir.
print(result)
print(soup.title)
print(soup.body)
print(soup.title.string)
result2 = soup.find_all('p') #tüm h2leri getirir 'h2'[0] ilk eleman
print(soup.div.findChildren()) # div içindeki tüm alt elemanları verir kod satırı aynı yerden başlarsa sbling eleman denir.

