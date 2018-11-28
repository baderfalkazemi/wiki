from django.shortcuts import render
from .models import Page
# Create your views here.
def detail_view(request,page_id):
	context = {
	"page":Page.objects.get(id=page_id)
	}
	return render(request,'detail.html', context)

def list_view(request):
	context = {
	"pages":Page.objects.all()
	}
	return render(request,'list.html', context)