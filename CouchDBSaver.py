from newspaper import Article
import sys
from datetime import datetime
import logging
import couchdb



class CouchDBSaver:
    def __init__(self, connectionString, dbName) -> None:
        couch = couchdb.Server(connectionString)
        db = couch[dbName]
        self.couchDbHandle = db
        self.logger = logging.getLogger('main')
        pass
    

    def Save(self, url, content):
        try:
            self.couchDbHandle.save({'_id': url, 'text': content})
            self.logger.info('Saved successfully url {}.'.format(url))
        except Exception as e:
            self.logger.error('Error when saving in db. Failed url {}. Exception {}'.format(url, e.message))

    def DoesArticleExist(self, url):
        try:
            entry = self.couchDbHandle.get(url)
            if entry is None:
                return False
            else:
                return True
        except Exception as e:
            self.logger.error('Something wrong happened when checking for id. Exception {}'.format(e.message))
