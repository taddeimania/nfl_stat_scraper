from django.conf.urls import patterns, include, url
from nfl.scraper import views as scraper_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', scraper_views.ScraperView.as_view()),
    # url(r'^$', 'nfl.views.home', name='home'),
    # url(r'^nfl/', include('nfl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
