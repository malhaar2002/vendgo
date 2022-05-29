from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.show_dash),
    path('load-vendors/', views.load_vendors, name='ajax_load_vendors'),
    path('load-bands/', views.load_bands, name='ajax_load_bands'),
    path('request/', views.index),
    path('find_bid/', views.all_av_bids),
    path('find_bid/view_bid/', views.view_bid),
]