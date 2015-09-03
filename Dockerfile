FROM python:2.7

RUN  echo 'Acquire::http { Proxy "http://172.17.2.78:3142"; };' >> /etc/apt/apt.conf.d/01proxy

RUN apt-get update
RUN apt-get autoremove -y
RUN apt-get install -y python-pip
RUN pip install scrapy
RUN pip install ipython
RUN pip install openpyxl
RUN pip install validate_email
RUN pip install scrapyd
RUN pip install pyDNS
RUN pip install shub
RUN pip install beautifulsoup4
RUN pip install scrapyd-client

CMD scrapy
