from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category,Paper
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from markdown import markdown

def index(request):
    CategoryList = Category.objects.all()
    PaperList = Paper.objects.all().order_by('-update_time')
 #   PaperList2 = []
 #   for paper in  PaperList:
 #       paper.content =  markdown(paper.content)
 #       PaperList2.append(paper)
#    paginator = Paginator(PaperList, 3)
#    page = request.GET.get('page')
#    try:
#        contacts = paginator.page(page)
#    except PageNotAnInteger:
#        contacts = paginator.page(1)
#    except EmptyPage:
#        contacts = pagintor.page(paginator.num_pages)
    return render(request, 'index.html', {'CategoryList':CategoryList ,'PaperList': PaperList})

    #return render(request, 'index.html', {'CategoryList':CategoryList, 'contacts':contacts})
    #return render(request, 'index.html', {'CategoryList':CategoryList, 'PaperList':PaperList})

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
    paper = Paper.objects.filter(pk=paper_id)
    return render(request, 'paper_detail.html', {'paper': paper[0]})
def aboutme(request):
    return render(request, 'aboutme.html')


