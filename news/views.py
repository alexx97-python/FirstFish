from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News, Rubric


class NewsView(ListView):
    model = News
    template_name = 'news/news_summary.html'
    paginate_by = 2


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context