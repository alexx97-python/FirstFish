from django.urls import path, include
from .views import NewsView,\
    NewsDetailView


urlpatterns = [
    path('all-newses/', NewsView.as_view(), name='all_newses'),
    path('detail/<uuid:pk>', NewsDetailView.as_view(), name='detail')
]