from django.urls import path
from vendor import views

urlpatterns = [
    path('', views.vendor_dashboard, name='vendor_dashboard'),
    path('view_order', views.view_order, name='view_order'),
    path('view_catalogue', views.view_catalogue, name='view_catalogue'),
    path('add_band', views.add_band, name='add_band')
]
