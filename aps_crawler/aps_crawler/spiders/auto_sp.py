from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class Crawlingspider(CrawlSpider):
    name = 'autocrawler'
    allowed_domains = ['autogidas.lt']
    start_urls = ['https://autogidas.lt/skelbimai/automobiliai/']

    rules = (
        Rule(LinkExtractor(allow="skelbimai/"), callback = "parse_item"),
    )

    # custom_settings = {
    #     'USER_AGENT': 'msnbot',
    #     'ROBOTSTXT_OBEY': True,
    # }


    def parse_item(self, response):
        title = response.css("h2.item-title::text").get()
        print("Title: ", title)  # Spausdina pavadinimą į konsolę

        yield {
            "title": response.css("h2.item-title::text").get(),
            "Years": response.css("span.icon.param-year b::text").get(),
            "Rida": response.css("span.icon.param-mileage b::text").get()
        }


