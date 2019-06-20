import scrapy


class PlayerStatsSpider(scrapy.Spider):
    name = "player_stats"
    start_urls = ["https://www.basketball-reference.com/leagues/NBA_2019_per_game.html"]

    def parse(self, response):
        for player in response.xpath("//tr[@class='full_table']"):
            yield {
                "player-name": player.xpath(".//td[@data-stat='player']/a/text()").extract_first(),
                "player-pos": player.xpath(".//td[@data-stat='pos']/text()").extract_first(),
                "player-age": player.xpath(".//td[@data-stat='age']/text()").extract_first()
            }
