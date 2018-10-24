from django.shortcuts import render
from .forms import SubscriberForm
from products.models import Product

def article(request):
	name = "my dear Feldjer"
	current_day = "07.05.2018"
	form = SubscriberForm(request.POST or None)
	
	if request.method == "POST" and form.is_valid():
		print (request.POST)
		print (form.cleaned_data)
		data = form.cleaned_data
		print (data["name"])
		
		new_form = form.save()
		
	return render(request, 'articles/base.html', locals())

	
def home(request):
	products = Product.objects.filter(is_active=True)
	return render(request, 'articles/home.html', locals())
	
def list(request):
	return render(request, 'articles/list.html', locals())