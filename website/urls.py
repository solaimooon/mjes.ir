from django.urls import path
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from .sitemaps import *

app_name = 'website'

sitemaps = {
    'static': StaticViewSitemap(),
}
urlpatterns = [

    path('', index, name='index'),
    path('live/', live, name='live'),
    path('report/', report, name='report'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('archive/<str:media_slug>/', media_single, name='single_media'),
    path('<str:category_slug>/', year_list, name='occasion_years'),
    path('<str:category_slug>/year:<int:year>/', occasion_list, name='occasion_list'),
    path('<str:category_slug>/<str:occasion_slug>/', night_list, name='night_list'),
    path('<str:category_slug>/<int:year>/<str:occasion_slug>/<str:night_slug>/', media_list, name='media_list'),

]
