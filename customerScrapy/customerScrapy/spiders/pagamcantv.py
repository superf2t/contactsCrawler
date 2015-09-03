# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class PagamcantvSpider(CrawlSpider):
    name = 'pagamcantv'
    allowed_domains = ['http://www.pac.com.ve/']
    start_urls = ['http://www.http://www.pac.com.ve//']
    custom_settings = {
        'DEPTH_LIMIT': 0,
        'DEPTH_PRIORITY': 0,
        'USER_AGENT': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/535.24 (KHTML, like Gecko)"
                      "Chrome/39.0.2171.95 Safari/537.36",
        'CONCURRENT_REQUESTS': 32,
        # 'DOWNLOAD_DELAY': 0.25,
        'COOKIES_ENABLED': False,
    }
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = CustomerscrapyItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
