from bs4 import element
import feedparser
import logging
import couchdb
import sys
import random
import time

from newspaper import article
from articles import ArticleSaver
from datetime import datetime

logger = logging.getLogger('main')
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
fileHandler = logging.FileHandler(
    'logs\{:%Y-%m-%d-%H-%M-%S}.log'.format(datetime.now()))
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

couch = couchdb.Server('http://admin:couch8admin@127.0.0.1:5984/')
db = couch['newsqa']

articleSaver = ArticleSaver(db)

rss = ["http://www.blog.pythonlibrary.org/feed/"]
for rssKey in rss:
    logger.info('Processing RSS key {}'.format(rssKey))
    feed = feedparser.parse(rssKey)
    logger.info('Found {} keys in RSS'.format(len(feed["entries"])))
    for key in feed["entries"]:
        link = key["link"]
        logger.info('Processing {element}'.format(element=link))
        if articleSaver.DoesArticleExist(link):
            logger.info('URL {} already exist, exiting'.format(link))
        else:
            logger.info('URL {} does not exist. Processing'.format(link))
            sleepSeconds = random.randint(15, 40)
            logger.info('Sleeping for {} seconds.'.format(sleepSeconds))
            time.sleep(sleepSeconds)
            content = articleSaver.Process(link)
            articleSaver.Save(link, content)
            

