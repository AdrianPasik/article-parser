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



print(configuration["source"]["rss"][0])
minSleepInSeconds = int(configuration["sleep-seconds"]["min"])
maxSleepInSeconds = int(configuration["sleep-seconds"]["max"])
articleSaver = FileSystemSaver(configuration["file-persistence"]["path"])
articleParser = ArticleParser()

rss = configuration["source"]["rss"]
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
            logger.info('New URL found. Processing {}'.format(link))
            content = articleParser.Process(link)
            articleSaver.Save(link, content)
            sleepSeconds = random.randint(minSleepInSeconds, maxSleepInSeconds)
            logger.info('Sleeping for {} seconds.'.format(sleepSeconds))
            time.sleep(sleepSeconds)
            