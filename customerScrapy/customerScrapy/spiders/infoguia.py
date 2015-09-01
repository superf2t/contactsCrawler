# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from customerScrapy.items import InfoGuiaEmpresaItem, InfoGuiaCategoriaItem
import urlparse
import re
from BeautifulSoup import BeautifulSoup

class InfoguiaSpider(CrawlSpider):
    name = "infoguia"
    allowed_domains = ["paginasamarillas.infoguia.net"]
    custom_settings = {
        'DEPTH_LIMIT': 0,
        'DEPTH_PRIORITY': 0,
        'USER_AGENT': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko)"
                      "Chrome/19.0.1055.1 Safari/535.24",
        'CONCURRENT_REQUESTS': 32,
        'DOWNLOAD_DELAY': 0,
        'COOKIES_ENABLED': False,
    }
    start_urls = (
        'http://paginasamarillas.infoguia.net/',
        # 'http://paginasamarillas.infoguia.net/PagAm/PagAm.asp?cat=332&ciud=41&key=alquiler-de-carros-autos-vehiculos-santa-eduvigis-caracas&urb=20',
    )

    rules = (
        Rule(LinkExtractor(allow='cat_prin\.asp'), callback="parse_categoria", follow=True),
        Rule(LinkExtractor(allow='PagAm\.asp\?key'), callback="parse_subcategoria", follow=True),
        Rule(LinkExtractor(allow='PagAm\.asp\?emp'), callback="parse_empresa", follow=True),
    )

    def parse_empresa(self, response):
        parsedParams = urlparse.parse_qs(urlparse.urlparse(response.url).query)

        EmpresaItem = InfoGuiaEmpresaItem()
        # Datos de la empresa
        datosElement = response.xpath('//div[@class="datos-sede"]')
        EmpresaItem['nombre'] = datosElement.xpath('b/text()')[0].extract()
        if datosElement.xpath('div[@id="tlf1"]/text()').extract():
            EmpresaItem['telefonos'] = datosElement.xpath('div[@id="tlf1"]/text()').extract()
        if response.xpath('//div[@class="gris-secun info-aviso border-box"]/text()').extract():
            EmpresaItem['actividad'] =  "".join(response.xpath('//div[@class="gris-secun info-aviso border-box"]/text()').extract()).strip("\r\n\t").strip(' \n\r\t')

        if response.xpath('//div[@id="dir1"]/text()').extract():
            EmpresaItem['direccion'] = response.xpath('//div[@id="dir1"]/text()').extract()

        # Medios de comunicación
        contactElement = response.xpath('//div[@class="link-cuadro-contactar"]')
        if contactElement.xpath('a[@id="contactemp"]/text()').extract():
            EmpresaItem['email'] = contactElement.xpath('a[@id="contactemp"]/text()').extract()
        if contactElement.xpath('a[@id="webemp"]/text()').extract():
            EmpresaItem['website'] = contactElement.xpath('a[@id="webemp"]/text()').extract()
        if contactElement.xpath('a[@id="webmini"]/text()').extract():
            EmpresaItem['webmini'] = contactElement.xpath('a[@id="webmini"]/text()').extract()

        for selector in contactElement.xpath('a/@href'):
            link = selector.extract()
            if re.search('facebook', link):
                EmpresaItem['facebook'] = link
            elif re.search('twitter', link):
                EmpresaItem['twitter'] = link
            elif re.search('instagram', link):
                EmpresaItem['instagram'] = link

        EmpresaItem['id_ciudad'] = parsedParams['ciud']
        EmpresaItem['id_cliente'] = parsedParams['clte']

        # self.logger.info("Empresa: %s", response.url)
        yield EmpresaItem

    def parse_categoria(self, response):
        parsedParams = urlparse.parse_qs(urlparse.urlparse(response.url).query)

        CategoriaItem = InfoGuiaCategoriaItem()
        CategoriaItem['id_categoria'] = parsedParams['c']
        CategoriaItem['nombre'] = response.xpath('//a[@class="link-sitemap"]/text()').extract()[1].strip(' \r\n\t')
        yield CategoriaItem

    def parse_subcategoria(self, response):
        parsedParams = urlparse.parse_qs(urlparse.urlparse(response.url).query)
        
        CategoriaItem = InfoGuiaCategoriaItem()
        CategoriaItem['nombre'] = parsedParams['key']
        CategoriaItem['id_categoria'] = parsedParams['cat']
        CategoriaItem['ciudad'] = parsedParams['ciud']

        ids = []
        for parse in response.xpath('//a[@name]').extract():
            l = BeautifulSoup(parse)
            ids.append(l.a['name'])
        CategoriaItem['empresas'] = ', '.join(ids)

        try:
            CategoriaItem['urbanismo'] = parsedParams['urb']
        except KeyError:
            pass

        yield CategoriaItem