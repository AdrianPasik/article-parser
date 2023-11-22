from newspaper import Article
import sys
from datetime import datetime
import logging



class FileSystemSaver:
    def __init__(self, path) -> None:
        self.filePath = path
        self.logger = logging.getLogger('main')
        self.logger.info('File system object initialized with {}'.format(path))
        pass
    

    def Save(self, url, content):
        try:
            self.logger.info('Saved successfully url {}.'.format(url))
        except Exception as e:
            self.logger.error('Error when saving in db. Failed url {}. Exception {}'.format(url, e.message))

    def DoesArticleExist(self, url):
        try:
            self.logger.error('Article does not exist')
        except Exception as e:
            self.logger.error('Something wrong happened when checking for id. Exception {}'.format(e.message))
