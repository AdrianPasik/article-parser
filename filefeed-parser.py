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
    'logs\\{:%Y-%m-%d-%H-%M-%S}.log'.format(datetime.now()))
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)



minSleepInSeconds = int(configuration["sleep-seconds"]["min"])
maxSleepInSeconds = int(configuration["sleep-seconds"]["max"])
articleSaver = FileSystemSaver(configuration["file-persistence"]["path"])
articleParser = ArticleParser()

pathToFeed = configuration["source"]["file"][0]
with open(pathToFeed) as file:
    lines = [line.rstrip() for line in file]

for feedLine in lines:
    logger.info('Processing File feed key {}'.format(feedLine)) 
    if articleSaver.DoesArticleExist(feedLine):
        logger.info('URL {} already exist, exiting'.format(feedLine))
    else:
        logger.info('New URL found. Processing {}'.format(feedLine))
        content = articleParser.Process(feedLine)
        articleSaver.Save(feedLine, content)
        sleepSeconds = random.randint(minSleepInSeconds, maxSleepInSeconds)
        logger.info('Sleeping for {} seconds.'.format(sleepSeconds))
        time.sleep(sleepSeconds)
