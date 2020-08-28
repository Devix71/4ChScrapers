import json
import os

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.settings.default_settings import USER_AGENT
from scrapy.utils.project import get_project_settings

'''
This script is using the Scrapy library in order to parse a single user-specified thread from 4chan. At the moment it 
it prints replies in a formatted .json file, working on adding it the ability of downloading images too.
'''


# Checking if the file exists, if it exists, it deletes it and makes another, if it doesn't, it creates it

def scraperr(add, path, name):
    if not os.path.exists(path + name + ".json"):
        with open(path + name + ".json", "w") as file:
            file.write("")
    else:
        os.remove(path + name + ".json")
        os.remove(path + name + "fromattedReplies.json")
        with open(path + name + ".json", "w") as file:
            file.write("")

    s = get_project_settings()
    s['FEED_FORMAT'] = 'json'
    s['LOG_LEVEL'] = 'INFO'
    s['FEED_URI'] = "file:///" + path + name + "raw.json"
    s['LOG_FILE'] = path + name + 'Q1.log'

    # User input for setting the scraping destination

    proc = CrawlerProcess(s)
    add

    # Configuring the scraping bot

    BOT_NAME = 'Leaf'
    SPIDER_MODULES = ['Leaf.spiders']
    NEWSPIDER_MODULE = 'Leaf.spiders'
    DOWNLOAD_DELAY = 2
    ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

    class post(scrapy.Item):
        postNum = scrapy.Field()
        replyNum = scrapy.Field()
        quotedText = scrapy.Field()
        postText = scrapy.Field()

    # data format input class

    class Leaf(scrapy.Spider):
        name = 'threads'
        start_urls = [
            add
        ]
    # functions for formatting the json
        def open_spider(self, spider):
            self.file = open(path + name + "fromattedReplies.json", 'w')
            self.file.write("[")

        def close_spider(self, spider):
            self.file.write("]")
            self.file.close()

        def process_item(self, item):
            line = json.dumps(
                dict(item),
                sort_keys=True,
                indent=4,
                separators=(',', ': ')
            ) + ",\n"

            self.file.write(line)
            return item

        def parse(self, response):
            self.open_spider(Leaf)
            for P in response.xpath("/html[1]/body[1]/form[2]/div[1]/div[1]/div[1]/div[1]/div[3]"):
                yield {
                    'OP NUMBER': P.xpath(
                        '/html[1]/body[1]/form[2]/div[1]/div[1]/div[1]/div[1]/div[3]/span[4]/a[2]/text()').get(),
                    'OP title': P.xpath(
                        '/html[1]/body[1]/form[2]/div[1]/div[1]/div[1]/div[1]/div[3]/span[1]/text()').get(),
                    'Op text': P.xpath(
                        '/html[1]/body[1]/form[2]/div[1]/div[1]/div[1]/div[1]/blockquote[1]/text()').get(),
                    'OP picture': P.xpath(
                        '/html[1]/body[1]/form[2]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/img[1]/@src').get()
                }

            for a in range(0, 500):
                Path = "/html[1]/body[1]/form[2]/div[1]/div[1]/div[" + str(a) + "]/div[2]"
                for thread in response.xpath(Path):
                    reply = post()
                    reply['postNum'] = thread.xpath(Path + '/div[2]/span[3]/a[2]/text()').get(),
                    reply['replyNum'] = thread.xpath(Path + '/blockquote[1]/a[1] /text()').get(),
                    reply['quotedText'] = thread.xpath(Path + '/blockquote[1]/span[1]/text()').get(),
                    reply['postText'] = thread.xpath(Path + '/blockquote[1]/text()').get()
                    # item['postPicture'] = thread.xpath(
                    #  path + '/html[1]/body[1]/form[2]/div[1]/div[1]/div[18]/div[2]/div['
                    #    '3]/a[1]/img[1]/@src').get() or "null"
                    self.process_item(reply)
                    yield reply

            self.close_spider(Leaf)

    # setting the browser used for scraping

    process = CrawlerProcess(s, {
        USER_AGENT: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/61.0.3163.100 Safari/537.36 '

    })
    # Starting the scraping

    process.crawl(Leaf)
    process.start()
