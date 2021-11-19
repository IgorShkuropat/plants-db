from django.urls import path
from . import views
from .views import SearchResultsView


urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about),
    path('search_result', SearchResultsView.as_view(), name='search')
]


