# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PaginasAmarillasDominicanaContacto(scrapy.Item):
    nombre = scrapy.Field()
    email = scrapy.Field()
    website = scrapy.Field()
    direccion = scrapy.Field()

class InfoGuiaEmpresaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nombre = scrapy.Field()
    telefonos = scrapy.Field()
    actividad = scrapy.Field()

    direccion = scrapy.Field()

    email = scrapy.Field()
    website = scrapy.Field()
    facebook = scrapy.Field()
    twitter = scrapy.Field()
    instagram = scrapy.Field()
    webmini = scrapy.Field()

    id_ciudad = scrapy.Field()
    id_cliente = scrapy.Field()

class InfoGuiaCategoriaItem(scrapy.Item):
	nombre = scrapy.Field()
	id_categoria = scrapy.Field()
	subcategorias = scrapy.Field()
	empresas = scrapy.Field()
	ciudad = scrapy.Field()
	urbanismo = scrapy.Field()
