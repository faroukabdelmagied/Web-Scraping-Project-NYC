from rocket_league.items import RocketLeagueItem
from scrapy import Spider, Request

class RocketleaugeSpiderI(Spider):
    name = 'rocketleague_spider'
    allowed_urls = ['https://rocketleague.tracker.network']
    start_urls = ['https://rocketleague.tracker.network/rocket-league/leaderboards/stats/all/default']

    def parse(self,response):
        result_urls = [f'https://rocketleague.tracker.network/rocket-league/leaderboards/stats/all/default?page={i+1}' for i in range(0,100)]

        for url in result_urls:
            yield Request(url=url, callback=self.parse_results_page)

    def parse_results_page(self, response):
        # product_urls = response.xpath('//div[@class="text"]/a[1]/@href').extract()
        # products_urls = ['https://rocketleague.tracker.network' + url + '/overview' for url in product_urls]

        players = response.xpath('//tbody//tr')

        for player in players:
            Players_urls = player.xpath('.//a[1]/@href').extract()
            Players_urlsz = ['https://rocketleague.tracker.network' + url + '/overview' for url in Players_urls]
            Player_name = player.xpath('.//span[@class="trn-ign__username"]/text()').extract_first()
            Rank = player.xpath('.//td[@class="rank"]//text()').extract_first().strip() 
            Goals = player.xpath('.//td[@class="stat"]//text()').extract_first().strip()
            meta = {'Player_name' : Player_name,'Rank' : Rank,'Goals' : Goals}
            for url in Players_urlsz:
                yield Request(url = url, callback=self.parse_product_page, meta = meta)
        
            # item = RocketLeagueItem()
            # item['Player_name'] = meta['Player_name']
            # item['Rank'] = meta['Rank']
            # item['Goals'] = meta['Goals']

            

            # print('='*50)
            # print(meta)
            # print('='*50)

        
            # yield Request(url = Players_urlsz, callback=self.parse_product_page, meta = meta)

    def parse_product_page(self, response):
        Player_name = response.meta['Player_name']
        Rank = response.meta['Rank']
        Goals = response.meta['Goals']
        Wins = response.xpath('//div[@class="numbers"]//span[@class="value"]/text()').extract()[0]
        Goal_Shot_Ratio = response.xpath('//div[@class="numbers"]//span[@class="value"]/text()').extract()[1] 
        Shots = response.xpath('//div[@class="numbers"]//span[@class="value"]/text()').extract()[3]
        Assists = response.xpath('//div[@class="numbers"]//span[@class="value"]/text()').extract()[4] 
        Saves = response.xpath('//div[@class="numbers"]//span[@class="value"]/text()').extract()[5]
        MVPs = response.xpath('//div[@class="numbers"]//span[@class="value"]/text()').extract()[6]
        TRN_Score = response.xpath('//div[@class="numbers"]//span[@class="value"]/text()').extract()[7]
        
        # print('='*50)
        # print(Player_name)
        # print('='*50)
        

        # yield{'Player_name' : Player_name,'Rank' : Rank,'Goals' : Goals}

        item = RocketLeagueItem()
        item['Player_name'] = Player_name
        item['Rank'] = Rank
        item['Goals'] = Goals
        item['Wins'] = Wins
        item['Goal_Shot_Ratio'] = Goal_Shot_Ratio
        item['Shots'] = Shots
        item['Assists'] = Assists
        item['Saves'] = Saves
        item['MVPs'] = MVPs
        item['TRN_Score'] = TRN_Score
        yield item
