from django.shortcuts import render


# Create your views here.
def base_view_portfolio(request):
    return render(request, 'portfolio_base.html', {})
