from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#django.template.Library.filter() for register function as filter
register = template.Library()

@register.simple_tag(takes_context=True)
def pagination(context, paperList, pageNum):
    paginator = Paginator(paperList, pageNum)
    page = context['request'].GET.get('page')
    try:
        contacts = paginator.page(page)
        context['current_page'] = page
    except PageNotAnInteger:
        contacts = paginator.page(1)
        context['current_page'] = 1
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    context['total_page'] = range(1,paginator.num_pages+1) 
    context['contacts'] = contacts

    return ''




###################Learn Custom Template filter/tags#####################
@register.filter
def lower(value):
    return value.lower()
@register.simple_tag(takes_context=True)
def my_tag(context, var):
    #context['string'] = string.lower()
    context['string'] = var.upper()
    #return var.lower() 
    return ''
@register.tag
def upper(parser, token):
    nodelist = parser.parse(('endupper',))
    parser.delete_first_token()
    return UpperNode(nodelist)
class UpperNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        output = self.nodelist.render(context)
        return output.upper()

