from django import template
from blog.models import Paper
from django.urls import reverse

register = template.Library()

#get previous paper by search database
@register.filter()
def has_previous_paper(paper_pk):
    total_paper_list_pk=[]
    for p in Paper.objects.all():
        total_paper_list_pk.append(p.pk)
    total_paper_list_pk.sort()
    if paper_pk > 1:
        current_paper_pk_index=total_paper_list_pk.index(paper_pk)
        #first paper
        if current_paper_pk_index == 0:
            return False
        else:
            return True
    else:
        return False

#get previous paper by search database
def get_previous_pk(paper_pk):
    total_paper_list_pk=[]
    for p in Paper.objects.all():
        total_paper_list_pk.append(p.pk)
    total_paper_list_pk.sort()
    #get current paper pk index of list
    current_paper_pk_index=total_paper_list_pk.index(paper_pk)
    #get previous paper pk
    previous_paper_pk=total_paper_list_pk[current_paper_pk_index-1]
    return previous_paper_pk

@register.filter()
def get_previous_url(paper_pk):
    previous_paper_pk=get_previous_pk(paper_pk)
    return reverse('blog:paper', kwargs={'paper_id':previous_paper_pk})

@register.filter()
def get_previous_name(paper_pk):
    previous_paper_pk=get_previous_pk(paper_pk)
    previous_paper=Paper.objects.filter(pk=previous_paper_pk)[0]
    return previous_paper.title

@register.filter()
def has_next_paper(paper_pk):
    total_paper_list_pk=[]
    for p in Paper.objects.all():
        total_paper_list_pk.append(p.pk)
    total_paper_list_pk.sort()
    current_paper_pk_index=total_paper_list_pk.index(paper_pk)
    #first paper
    if current_paper_pk_index == len(total_paper_list_pk)-1:
        return False
    else:
        return True

def get_next_pk(paper_pk):
    total_paper_list_pk=[]
    for p in Paper.objects.all():
        total_paper_list_pk.append(p.pk)
    total_paper_list_pk.sort()
    #get current paper pk index of list
    current_paper_pk_index=total_paper_list_pk.index(paper_pk)
    #get previous paper pk
    next_paper_pk=total_paper_list_pk[current_paper_pk_index+1]
    return next_paper_pk

@register.filter()
def get_next_url(paper_pk):
    next_paper_pk=get_next_pk(paper_pk)
    return reverse('blog:paper', kwargs={'paper_id':next_paper_pk})

@register.filter()
def get_next_name(paper_pk):
    next_paper_pk=get_next_pk(paper_pk)
    next_paper=Paper.objects.filter(pk=next_paper_pk)[0]
    return next_paper.title


