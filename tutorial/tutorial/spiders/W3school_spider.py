#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scrapy.spider import Spider
import logging; logging.basicConfig(level=logging.INFO, filename=r'mylog.txt')

class W3schoolSpider(Spider):
	"""docstring for DmozSpider"""
	name = 'w3school'
	allowed_domains = ["w3school.com.cn"]
	start_urls = [
		"http://www.w3school.com.cn/jquery/"
	]
	def parse(self, response):
		logging.info('response url as %s'%response.url)
		filename = response.url.split("/")[-2]
		open(filename, 'wb').write(response.body)