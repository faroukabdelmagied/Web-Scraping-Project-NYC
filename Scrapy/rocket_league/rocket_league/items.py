# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RocketLeagueItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Player_name = scrapy.Field()
    Rank = scrapy.Field()
    Goals = scrapy.Field()
    Wins = scrapy.Field()
    Goal_Shot_Ratio = scrapy.Field()
    Shots = scrapy.Field()
    Assists = scrapy.Field()
    Saves = scrapy.Field()
    MVPs = scrapy.Field()
    TRN_Score = scrapy.Field()