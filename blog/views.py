from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category,Paper,Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from markdown import markdown
import datetime
def index(request):
    CategoryList = Category.objects.all()
    TagList = Tag.objects.all()
    PaperList = Paper.objects.all().order_by('-created_time')
    #get a paper created_time list
    Dates = Paper.objects.datetimes('created_time', 'month', order='DESC')
    return render(request, 'index.html',
        {'CategoryList':CategoryList,
         'PaperList': PaperList,
         'Dates': Dates,
         'TagList': TagList})

def test(request):
    return render(request, 'test.html', {'teststring':"Xstring"})

#def category(request):
#    CategoryList = Category.objects.all()
#    return render(request, 'category.html', {'CategoryList':CategoryList})

def category(request):
    CategoryList = Category.objects.all()
    return render(request, 'category.html', {'CategoryList':CategoryList})

def category_detail(request, category_id):
    category = Category.objects.get(pk=category_id)
    papers = Paper.objects.filter(category=category)
    return render(request, 'category_detail.html', {'papers': papers})

def paper_detail(request, paper_id):
    paper = Paper.objects.filter(pk=paper_id)[0]
    paper.click += 1
    paper.save()
    return render(request, 'paper_detail.html', {'paper': paper})

def aboutme(request):
    return render(request, 'aboutme.html')

def archive(request):
    dates = Paper.objects.datetimes('created_time', 'month', order='DESC')
    return render(request, 'archive.html', {'dates':dates})

def archive_detail(request, created_year, created_month):
    #papers_of_year_month_list = Paper.objects.filter(
    #    created_time=datetime(created_year, created_month))
    papers_of_year_month_list = Paper.objects.filter(
        created_time__year=created_year,
        created_time__month=created_month)
    return render(request, 'archive_detail.html',
                  {'papers': papers_of_year_month_list})

def tags(request, tag_id):
    tags = Tag.objects.get(pk=tag_id)
    papers = Paper.objects.filter(tags=tags)
    return render(request, 'tags.html', {'papers': papers})


