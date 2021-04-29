import scrapy 
import asyncio
from twisted.internet import asyncioreactor
scrapy.utils.reactor.install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
is_asyncio_reactor_installed = scrapy.utils.reactor.is_asyncio_reactor_installed()
print(f"Is asyncio reactor installed: {is_asyncio_reactor_installed}")
from twisted.internet import reactor


from scrapy import spiderloader
from scrapy.utils import project
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor, defer
from scrapy.utils.log import configure_logging
import logging

from datetime import datetime

import scrapy 
import asyncio
from twisted.internet import asyncioreactor
scrapy.utils.reactor.install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
is_asyncio_reactor_installed = scrapy.utils.reactor.is_asyncio_reactor_installed()
from apscheduler.schedulers.twisted import TwistedScheduler


scheduler = TwistedScheduler(reactor=reactor)

@defer.inlineCallbacks
def crawl():
    #configure_logging()
    runner = CrawlerRunner()
    settings = project.get_project_settings()
    spider_loader = spiderloader.SpiderLoader.from_settings(settings)
    spiders = spider_loader.list()
    classes = [spider_loader.load(name) for name in spiders]
    for my_spider, spider_name in zip(classes,spiders):
        print(spider_name)
        logging.info(spider_name)
        #logging.info(f"Name of the active spider: "{spider_name})
        yield runner.crawl(my_spider)


def main():
    configure_logging()
    scheduler = TwistedScheduler()
    scheduler.add_job(crawl, 'interval', seconds=60, next_run_time=datetime.now())
    scheduler.start()
    reactor.run()

if __name__ == '__main__':
    main()