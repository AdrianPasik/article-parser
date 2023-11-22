from articleParser import ArticleParser
import feedparser
import logging
from FileSystemSaver import FileSystemSaver
import sys
import random
import time
import yaml
from newspaper import article
from datetime import datetime

import yaml
with open('config.yml', 'r') as file:
    configuration = yaml.safe_load(file)

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




articleSaver = FileSystemSaver(configuration["file-persistence"]["path"])


rss = ["http://www.blog.pythonlibrary.org/feed/"]
""" for rssKey in rss:
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
            time.sleep(sleepSeconds) """
            #content = articleSaver.Process(link)
            #articleSaver.Save(link, content)
            

