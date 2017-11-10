# -*- coding: utf-8 -*-
import scrapy
import html2text


class BanksSpider(scrapy.Spider):
#     имя будет использоваться при вызове команды crawl
    name = "banks"
#     Зададим начальную страницу
    start_urls = [
        'http://www.banki.ru/services/responses/',
    ]
# Распарсим страницы с отзывами
    def parsePage(self, response):

        if response.status != 400:

            h = html2text.HTML2Text()
            h.ignore_links = True
            
            #if len(get_next) > 1:
            #    current_number = int(get_next[-1])
            #else:
            #    current_number = 1
            with open("bag.txt", "w") as f:
                print >> f, "start"
            for index, tr in enumerate(response.xpath('//tbody/tr')):
                with open("bag.txt", "a") as f:
                    print >> f, "index = " + str(index)
                    print >> f, tr
                    
                       
                

# Распарсим главную странцу
    def parse(self, response):

        page = "http://www.banki.ru/services/responses/"
        return scrapy.Request(page, callback=self.parsePage)