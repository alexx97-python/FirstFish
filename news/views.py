from django.shortcuts import render
from django.views.generic import ListView
from .models import News


class NewsView(ListView):
    model = News
    template_name = 'news/news_summary.html'
    paginate_by = 9
