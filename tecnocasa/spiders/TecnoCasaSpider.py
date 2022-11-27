# -*- coding: utf-8 -*-

import scrapy
from scrapy_selenium import SeleniumRequest
from tecnocasa.items import Tecnocasa


class TecnoCasaSpider(scrapy.Spider):
    name = 'tecnocasa'

    def start_requests(self):
        url = 'https://www.tecnocasa.es/venta/inmuebles/comunidad-de-madrid/madrid.html'
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        # XPATH selector to get each book url
        for link in response.xpath('//*[@class="estate-card"]/a/@href').extract():
            yield SeleniumRequest(url=link, callback=self.parse_house)
        next_page = response.xpath('//*[@class="pagination"]//a[.=">"]/@href').extract()

        if next_page:
            yield SeleniumRequest(url=next_page[0], callback=self.parse)

    def parse_house(self, response):
        # Function to scrap each field of data
        title = response.xpath("//*/h1[@class='estate-title']/text()").extract_first()
        address = response.xpath("//*/h2[@class='estate-subtitle']/text()").extract_first()
        price = response.xpath("//*/span[@class='current-price']/text()").extract_first()
        surface = response.xpath("//*[@class='estate-card-data-element estate-card-surface']/span/text()").extract_first()
        rooms = response.xpath("//*[@class='estate-card-data-element estate-card-rooms']/span/text()").extract_first()
        baths = response.xpath("//*[@class='estate-card-data-element estate-card-bathrooms']/span/text()").extract_first()

        tecnocasa = Tecnocasa()
        tecnocasa['Title'] = title.replace('\n', "").strip()
        tecnocasa['Address'] = address.replace('\n', "").replace(",", "-").strip()
        tecnocasa['Price'] = price.replace('\n', "").strip()
        tecnocasa['Surface'] = surface.replace('\n', "").strip()
        tecnocasa['Rooms'] = rooms.replace('\n', "").strip()
        tecnocasa['Baths'] = baths.replace('\n', "").strip()

        yield tecnocasa
