import urllib2
from django.http import HttpResponse
from django.views.generic import View
from nfl.scraper import models as scraper_models
from bs4 import BeautifulSoup
from nfl.scraper.scraper import StatScraper

class ScraperView(View):

    def get(self, *args, **kwargs):
        for team in scraper_models.Team.objects.all():
            for page in scraper_models.Page.objects.all():
                url = "http://sportsillustrated.cnn.com/football/nfl/teams/stats/{}/{}/{}".format(team.season.year, team.name, page.page)
                site_to_scrape = BeautifulSoup(urllib2.urlopen(url))
                StatScraper(site_to_scrape, team, team.season)

        return HttpResponse("Successfully scraped SI.com")




