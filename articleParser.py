import logging
from newspaper import Article

class ArticleParser:
    def __init__(self) -> None:
        self.logger = logging.getLogger('main')
        pass
    def Process(self, url):
        try:
            article = Article(url)
            article.download()
            article.parse()
            self.logger.info('Processing succeded on url {}.'.format(url))
            return article.text.replace('\n', "").replace('\t', "")
        except Exception as e:
            self.logger.error('Processing failure - will return empty url. Failed url {}. Exception {}'.format(url, e.message))
            return ""
