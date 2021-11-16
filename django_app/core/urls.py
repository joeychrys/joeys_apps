from django.contrib import admin
from django.urls import path, include
from portfolio.views import base_view_portfolio
from shop.views import shop_view
# from minecraft.views import home_view_minecraft, news_view_minecraft

urlpatterns = [
    path('django/', base_view_portfolio, name="home"),
    path('volunteernow/', shop_view, name="shop"),
    path('django/admin/', admin.site.urls),
]
