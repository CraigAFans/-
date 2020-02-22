import requests
import re
import os
headers = {"User-Agent": "Mozilla ESR/18.05 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3",
           "Referer": "http://www.biquge.tv/"}
url = "http://www.biquge.tv/0_1/1.html"
r = requests.get("http://www.biquge.tv/0_1/1.html", headers=headers)
r.encoding = r.apparent_encoding
html = r.text
#print(html)
#mainContext = re.findall(r'<dt>.*?</dl>', html, re.S)
content = re.findall(r'<div id="content">(.*?)</div>', html, re.S)
#pattern = re.match(r'<div id="content">(.*?)</div>', html)
#content = re.findall(pattern, html)
#print(content)
title = re.findall(r'<h1>(.*?)</h1>', html, re.S)
with open('E:/E-book/literature/%s.txt' % title,'w', encoding='utf-8') as f:
    for i in content:
        print(i)
        f.write(i)
