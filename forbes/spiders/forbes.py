# Imports
import scrapy
import re

# pattern that reads all the characters inside an HTML tag
pattern='<[^<]+?>'

class SaasSpider(scrapy.Spider):
    name = 'forbes'
    start_urls = ['https://www.forbes.com/lists/global2000/',
                  ]
    
    def parse(self, response):
    
        for saas in response.css('.table-row'):
            orgName = re.sub(pattern, "", response.css('.organizationName').get())
            country = re.sub(pattern, "", response.css('.country').get())
            revenue = re.sub(pattern, "", response.css('.revenue').get())
            profit = re.sub(pattern, "", response.css('.profits').get())
            assets = re.sub(pattern, "", response.css('.assets').get())
            marketValue = re.sub(pattern, "", response.css('.marketValue').get())
            
            yield {
                'Org Name':orgName, 'Country':country, 'Revenue':revenue, 
                'Profit':profit, 'Assets':assets, 'Market Value': marketValue
            }
        