from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category,Paper

def index(request):
    return render(request, 'index.html')

def category(request):
    CategoryList = Category.objects.all()
    return render(request, 'category.html', {'CategoryList':CategoryList}) 

def category_detail(request):
    pass    
#    PaperList = Paper.objects.filter()
#    return  

#def paper(request):

