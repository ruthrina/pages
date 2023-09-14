from django.urls import path

from .views import homePageView
from .views import aboutPageView

urlpatterns=[
    path('', homePageView.as_view(), name = 'homePage'),
    path('about/', aboutPageView.as_view(), name = 'aboutPage'),
   
]