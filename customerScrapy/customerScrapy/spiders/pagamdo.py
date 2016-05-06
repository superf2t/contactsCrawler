# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from customerScrapy.items import PaginasAmarillasDominicanaContacto
import urlparse
import re
from bs4 import BeautifulSoup

class PaginasAmarillasDominicana(CrawlSpider):
    name = "PaginasAmarillasDominicana"
    allowed_domains = ["www.paginasamarillas.com.do"]
    custom_settings = {
        'DEPTH_LIMIT': 0,
        'DEPTH_PRIORITY': 0,
        'USER_AGENT': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko)"
                      "Chrome/19.0.1055.1 Safari/535.24",
        'USER_AGENT_LIST': [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7"
                "(KHTML, like GInfoGuiaCategoriaItemecko) Chrome/16.0.912.36 Safari/535.7",
            "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0)"
                "Gecko/16.0 Firefox/16.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3"
                "(KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko)"
                "Chrome/19.0.1055.1 Safari/535.24",
        ],
        'CONCURRENT_REQUESTS': 32,
        'DOWNLOAD_DELAY': 0,
        'COOKIES_ENABLED': False,
        'FEED_URI': 'PaginasAmarillasDominicana.json',
        'FEED_FORMAT': 'jsonlines',
    }
    start_urls = (
        #'http://www.paginasamarillas.com.do/',
        'http://www.paginasamarillas.com.do/DCaballeros-Trajes-Elegantes/alquiler-de-smoking/santo-domingo/es/contacto.html?classCode=129800',
    )

    rules = (
        Rule(LinkExtractor(allow='contacto\.html\?classCode'), callback="parse_contacto", follow=True),
        #Rule(LinkExtractor(allow='PagAm\.asp\?key'), callback="parse_subcategoria", follow=True),
        #Rule(LinkExtractor(allow='PagAm\.asp\?emp'), callback="parse_empresa", follow=True),
    )

    def parse_contacto(self, response):
        parsedParams = urlparse.parse_qs(urlparse.urlparse(response.url).query)

        ContactoItem = PaginasAmarillasDominicanaContacto()
        ContactoItem['nombre'] = "".join(response.xpath('//span[@itemprop="name"]/text()').extract()).strip('\r\n ')
        ContactoItem['direccion'] = "".join(response.xpath('//span[@itemprop="streetAddress"]/text()').extract() +
                                            response.xpath('//span[@itemprop="addressLocality"]/text()').extract()).strip('\r\n ')
        ContactoItem['email'] = "".join(response.xpath('//span[@itemprop="email"]/text()').extract()).strip('\r\n ')
        ContactoItem['website'] = "".join(response.xpath('//a[@itemprop="url"]/text()').extract()).strip('\r\n ')

        yield ContactoItem
