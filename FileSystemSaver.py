from newspaper import Article
import sys
from datetime import date
import logging
import os
import io
import json
import uuid



class FileSystemSaver:
    HISTORY_FILE='history.txt'

    def __init__(self, path) -> None:
        self.filePath = path
        self.logger = logging.getLogger('main')
        self.logger.info('File system object initialized with {}'.format(path))
        pass
    

    def Save(self, url, content):
        try:
            data = {
                'url': url,
                'content': content
            }
            filename = '{}.json'.format(uuid.uuid4().hex)
            path = os.path.join(self.filePath, filename)
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            self.logger.info('Saved successfully url {}.'.format(url))

            historyFilePath = os.path.join(self.filePath, self.HISTORY_FILE)
            with open(historyFilePath, 'a', encoding='utf-8') as historyFile:
                historyFile.write('{}\n'.format(url))
                self.logger.info('Saved into history file {}.'.format(url))
        except Exception as e:
            self.logger.error('Error when saving file. Failed url {}. Exception {}'.format(url, e.message))

    def DoesArticleExist(self, url):
        try:
            historyFilePath = os.path.join(self.filePath, self.HISTORY_FILE) 
            if os.path.isfile(historyFilePath) and os.path.isdir(self.filePath):
                with open(historyFilePath, 'r', encoding='utf-8') as historyFile:
                    lines = [line.rstrip() for line in historyFile]
                    if (url in lines):
                        return True
                    else:
                        return False
            else:
                with open(historyFilePath, 'w', encoding='utf-8') as historyFile:
                    self.logger.info('History file missing, creating')
                    return False
        except Exception as e:
            self.logger.error('Something wrong happened when checking for id. Exception {}'.format(e.message))
