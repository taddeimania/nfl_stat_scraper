from nfl.scraper import models as scraper_models

class StatScraper(object):

    def __init__(self, site, team, season):
        self.base_site = site
        self.site = site('tr')
        self.team = team
        self.season = season
        self.stat_categories = [u'Player']
        self.players = []
        self.parse_site()

    def parse_site(self):
        self.get_stat_categories()
        self.set_stats()

    def get_stat_categories(self):
        # scrapes header for page because many categories have same stat name
        # used to prepend stat category
        stat_grouping = self.base_site.find('h2').string

        categories = self.site[0].find_all('a')
        for category in categories:
            self.stat_categories.append(category.text)

        # our above hack doesn't fix punt/kick returns values so we are more specific
        # with this hack.
        if stat_grouping == "Returns":
            self.stat_categories[7] = 'Punt_Yards'
            self.stat_categories[8] = 'Punt_Avg'
            self.stat_categories[9] = 'Punt_Long'

        for i in range(1, len(self.site) - 1):
            player = {}
            for i, line in enumerate(filter(lambda a: a != '\n', self.site[i])):
                # go ahead and ignore player names, games played, and games started
                if self.stat_categories[i] not in ['Player', 'G', 'GS']:
                    search_string = "{}_{}".format(stat_grouping, self.stat_categories[i])
                else:
                    search_string = self.stat_categories[i]

                # another creepy hack thanks to player names coming in funky
                player[search_string] = line.string.replace(u'\xa0', u' ')
            self.players.append(player)


    def set_stats(self):
        for record in self.players:
            # get or create (new or update) player and stat objects to be updated with our stat stream
            player, _ = scraper_models.Player.objects.get_or_create(name=record['Player'], team=self.team)
            stat, _ = scraper_models.Stat.objects.get_or_create(player=player, player__team__season=self.season)

            for record_key in record.keys():
                # we just want to use the above player we grabbed
                if record_key == 'Player':
                    value = player
                else:
                    value = record[record_key]

                # update the stat object's attributes based on the mapping from the scraped page -> our model
                setattr(stat, scraper_models.stat_attr_map[record_key], value)

            stat.save()
