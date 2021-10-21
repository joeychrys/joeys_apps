import django
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect


# Create your views here.
def base_view_portfolio(request):
    submitted= False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/django/?submitted#contact")
    else:
        form = ContactForm
        if 'submitted' in request.GET:
            submitted= True
    context= {
        'form':form,
        'submitted': submitted,
    }
    return render(request, 'portfolio_base.html',context)
