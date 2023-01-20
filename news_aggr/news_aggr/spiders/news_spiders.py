import sys
from datetime import date
import scrapy

from news_aggr.items import NewsAggrItem

def get_date():
    today = date.today()
    return today.strftime('%#m-%d-%y') if sys.platform.startswith('win') else today.strftime('%-m-%d-%y')


class NewsBBCSpider(scrapy.Spider):
    name = "bbc_news"
    start_urls = [
            "https://www.bbc.com/news/world/europe",
        ]

    def parse(self, response):
        for article in response.xpath("//article"):
            title = article.xpath(".//span[@class='lx-stream-post__header-text gs-u-align-middle']/text()").get()
            brief = article.xpath(".//p[@class='lx-stream-related-story--summary qa-story-summary']/text()").get()

            yield NewsAggrItem(source="BBC",date=get_date(), title=title, brief=brief)


class NewsCNNSpider(scrapy.Spider):
    name = "cnn_news"
    start_urls = [
        f"https://edition.cnn.com/europe/live-news/russia-ukraine-war-news-{get_date()}",
    ]

    def parse(self, response):
        for article in response.xpath("//article"):
            title = article.xpath(".//header/h2[@class='sc-dfVpRl kvaBeP']/text()").get()
            brief = article.xpath(".//div[1]/p[@class='sc-gZMcBi "
                                       "render-stellar-contentstyles__Paragraph-sc-9v7nwy-2 dCwndB']/text()").get()

            yield NewsAggrItem(source="CNN", date=get_date(), title=title, brief=brief)
