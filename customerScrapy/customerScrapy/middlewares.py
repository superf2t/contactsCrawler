import os
import random

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(spider.settings.get('USER_AGENT_LIST'))
        if ua:
            request.headers.setdefault('User-Agent', ua)

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = spider.settings.get('HTTP_PROXY')     