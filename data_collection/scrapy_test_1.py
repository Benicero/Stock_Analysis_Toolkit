"""

run this file using:
    scrapy runspider scrapy_test_1.py -o <output filename>.json

This program will get the current price of every stock on the nasdaq
Not historical price, but i think this scrapy tool will be very helpful

"""

import scrapy
import json


class QuotesSpider(scrapy.Spider):
    AUTOTHROTTLE_ENABLED = True

    name = 'nasdaq_scrape'
    # load all 40,000+ companies from the nasdaq
    start_urls = [
        'https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&pagesize=50000'
    ]

    # get data for each, gets written to json file by scrapy
    def parse(self, response):
        for table in response.css('#CompanylistResults'):
            # alternating rows in the table have the stuff we actually want
            data_we_want = False
            for row in table.css('tr'):
                if data_we_want:
                    data_we_want = False
                    # get the data
                    data = {
                        'name'      : row.css(':nth-child(1) > a::text').get(),
                        'code'      : row.css(':nth-child(2) > h3 > a::text').get(),
                        'price'     : row.css(':nth-child(3)::text').get(),
                        'country'   : row.css(':nth-child(4)::text').get(),
                        'sector'    : row.css(':nth-child(6)::text').get(),
                    }
                    # clean tabs and whitespace
                    for key, val in data.items():
                        try:
                            data[key] = val.strip()
                        except AttributeError:
                            pass
                    yield data
                else:
                    data_we_want = True



