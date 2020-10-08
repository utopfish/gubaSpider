import scrapy
from gubaSpider.items import GubaspiderItem,ContentspiderItem,AuthorspiderItem

class GubaSpider(scrapy.Spider):
    name = 'guba'
    baseurl='http://guba.eastmoney.com'

    def start_requests(self):
        for i in range(1,10000):
            url="http://guba.eastmoney.com/list,zssh000001,f_{}.html".format(i)
            yield scrapy.Request(url, callback=self.parse)
        # author_url="https://i.eastmoney.com/3006113720930996"
        # yield scrapy.Request(author_url,callback=self.parse_author)
    def parse(self, response):
        for item in response.xpath('//div[@id="articlelistnew"]/div[@class="articleh "]'):
            guba=GubaspiderItem()
            guba['read_number']=item.xpath('span[@class="l1 a1"]/text()').extract_first()
            guba['command_number']=item.xpath('span[@class="l2 a2"]/text()').extract_first()
            guba['title']=item.xpath('span[@class="l3 a3"]/a/text()').extract_first()
            guba['title_url']=self.baseurl+item.xpath('span[@class="l3 a3"]/a/@href').extract_first()
            guba['author']=item.xpath('span[@class="l4 a4"]/a//text()').extract_first()
            guba['author_url']=item.xpath('span[@class="l4 a4"]/a/@href').extract_first()
            if guba['author_url'][0]=='/':
                guba['author_url']=self.baseurl+guba['author_url']
            guba['date']=item.xpath('span[@class="l5 a5"]/text()').extract_first()
            yield scrapy.Request(guba['title_url'],callback=self.parse_content)
            yield scrapy.Request(guba['author_url'],callback=self.parse_author)
            yield guba

    def parse_content(self,response):
        content=ContentspiderItem()
        content['title_url']=response._url
        content_tmp=response.xpath('//*[@id="post_content"]//text()').extract()
        content['content']='\n'.join(content_tmp).strip()
        yield content
    def parse_author(self,response):
        author=AuthorspiderItem()
        author['author_url']=response._url
        author['following_number']=response.xpath('//*[@id="tafollownav"]/p/span/text()').extract_first()
        author['follower_number']=response.xpath('//*[@id="tafansa"]/p/span/text()').extract_first()
        yield author


