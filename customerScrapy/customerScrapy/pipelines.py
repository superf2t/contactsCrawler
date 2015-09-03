# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()
# class Categoria(Base):
#     __tablename__ = 'categoria'

#     id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
#     name = Column(String(128))
#     ciudad = Column(Integer)
#     urbanismo = Column(String(50))
#     subcategorias = 
#     empresas = scrapy.Field()

#     def __repr__(self):
#             return "<Categoria(id='%s', name='%s')>" % (self.id, self.name)

class MysqlPipeline(object):

    def __init__(self):
        pass
        # self.engine = create_engine('mysql://scrapy:passwd@localhost/infoguia', echo=False)
        # self.Session = sessionmaker(bind=self.engine)

    def open_spider(self, spider):
        pass
        # self.session = self.Session()

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        return item
