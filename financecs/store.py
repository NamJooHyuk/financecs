#encoding: utf-8
from pymongo import MongoClient
from scrapy.conf import settings
client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
News_csDB = client[settings['MONGODB_DB']]
collect_cs_161213 = News_csDB[settings['MONGODB_COLLECTION']]