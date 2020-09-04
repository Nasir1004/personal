from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'cni/index.html')

def portfolio(request):
	return render(request, 'cni/portfolio.html')	
