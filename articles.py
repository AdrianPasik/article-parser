from newspaper import Article
import couchdb
url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
couch = couchdb.Server('http://admin:couch8admin@127.0.0.1:5984/')
db = couch['newsqa']
doesEntityExist = db.get(url)
if doesEntityExist is None:
	db.save({'_id': url, 'text': 'dummy'})
else:
	print('Entity exists')



""" url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
article = Article(url2)
article.download()
article.parse() """


# print(article.text)


class ArticleSaver:
	@staticmethod
	def Process(url):
		article = Article(url)
		article.download()
		article.parse().replace('\n',"").replace('\t',"")
	def Save(couchDbHandle, url, content):
		couchDbHandle.save({'_id': url, 'text': content})




		
