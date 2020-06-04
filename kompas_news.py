# -*- coding: UTF-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector

class KompassNewsSpider(scrapy.Spider):
    name = 'kompass_news'
    allowed_domains = ['web.archive.org']
    start_urls = [
        'https://web.archive.org/web/20190601051416/https://sains.kompas.com/read/2019/06/01/100600023/gletser-himalaya-mencair-800-juta-orang-di-asia-terancam'
    ]

    def __init__(self):
        options = Options()

        # prefs = {
        #      "translate_whitelists": {"id":"en"},
        #      "translate":{"enabled":"true"}
        #  }

        # options.add_experimental_option("prefs", prefs)
        options.headless = False

        driver = webdriver.Chrome(executable_path = './chromedriver.exe', options = options)
        driver.get('https://web.archive.org/web/20190601051416/https://sains.kompas.com/read/2019/06/01/100600023/gletser-himalaya-mencair-800-juta-orang-di-asia-terancam')

        self.html = driver.page_source
        driver.close()


    def parse(self, response):
        resp = Selector(text=self.html)
        yield{
            'title' : resp.xpath('//h1[@class="read__title"]/text()').get(),
            'contents' : resp.xpath('//div[@class="read__content"]/descendant::*/text()').getall()
        }
