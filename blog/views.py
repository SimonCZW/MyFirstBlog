from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category,Paper

def index(request):
    return render(request, 'index.html')

def category(request):
    CategoryList = Category.objects.all()
    return render(request, 'category.html', {'CategoryList':CategoryList}) 

def category_detail(request, category_id):
    category = Category.objects.get(pk=category_id)
    papers = Paper.objects.filter(category=category)
    return render(request, 'category_detail.html', {'papers': papers})

def paper_detail(request, paper_id):
    paper = Paper.objects.filter(pk=paper_id)
    return render(request, 'paper_detail.html', {'paper': paper[0]})


