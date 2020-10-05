from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('<slug:slug>', views.listing, name='listing-slug'),
    path('search', views.search, name='search'),

]