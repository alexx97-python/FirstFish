from django.urls import path, include
from .views import NewsView


urlpatterns = [
    path('all-newses/', NewsView.as_view(), name='all_newses')
]