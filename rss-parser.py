import feedparser
from articles import 
rss = 'http://www.blog.pythonlibrary.org/feed/'
feed = feedparser.parse(rss)
for key in feed["entries"]: 
    print(key["link"])