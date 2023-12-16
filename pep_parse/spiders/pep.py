import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://{}/'.format(domain) for domain in allowed_domains]

    def parse(self, response):
        """Собирает информацию об URL-адресах всех PEP"""
        pep_list = response.css(
            '#numerical-index table.pep-zero-table tbody tr'
        )
        for pep in pep_list:
            pep_link = pep.css('a::attr(href)').get()
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Собирает информацию со страницы конкретного PEP"""
        h1 = response.css('#pep-content > h1::text').get().split()
        number = h1[1]
        name = ' '.join(h1[3:])
        status = response.css('abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)
