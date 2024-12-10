import feedparser, datetime

uri="https://dose-blog.tistory.com"
feed = feedparser.parse(uri+"/rss")

markdown_text = """#dose-blog.tistory.com
## blog posts
"""

lst = []


for i in feed['entries']:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
