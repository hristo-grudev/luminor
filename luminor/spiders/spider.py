import scrapy

from scrapy.loader import ItemLoader
from ..items import LuminorItem
from itemloaders.processors import TakeFirst


class LuminorSpider(scrapy.Spider):
	name = 'luminor'
	start_urls = ['https://www.luminor.lv/lv/jaunumu-arhivs?field_news_category_tid=All']

	def parse(self, response):
		post_links = response.xpath('//a[@class="post__link clearfix post__link--dnb"]/@href')
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1[@class="no-margin"]/text()').get()
		description = response.xpath('//div[@class="l-content l-content--with-sidebar l-content--break-medium"]//text()').getall()
		description = ' '.join(description)
		date = response.xpath('//span[@class="date"]//text()').get()

		item = ItemLoader(item=LuminorItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
