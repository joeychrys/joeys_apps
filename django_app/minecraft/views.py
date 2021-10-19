from django.shortcuts import render
from .models import NewsPost


# Create your views here.
def home_view_minecraft(request):
    news = NewsPost.objects.latest("id")

    context = {
        'version': news.version,
        'description': news.description,
    }
    return render(request, 'minecraft_home.html', context=context)


def news_view_minecraft(request):
    news = NewsPost.objects.all().order_by('-id')

    context = {
        'news': news,
    }
    return render(request, 'minecraft_news.html', context=context)
