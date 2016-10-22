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
        context['current_page'] = int(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
        context['current_page'] = 1
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    context['first_page'] = 1
    context['last_page'] = paginator.num_pages
    context['total_page'] = range(1,paginator.num_pages+1) 
    context['contacts'] = contacts

    limit_length = 2
    #get left page list
    try:
        context['left_pages'], context['LeftMoreTag'] = get_left(int(page), limit_length)
    except:
        context['left_pages'], context['LeftMoreTag'] = get_left(1, limit_length)


#    context['right_pages'] = get_right(int(page), 2)
    return ''

#return left page list
def get_left(current_page, limit_page):
    #judge limit_page len
    #further more
    if len(range(2, current_page)) > limit_page:
        LeftPageList = range(2, current_page+1)[-1-limit_page:-1] 
        LeftMoreTag = True  
    
    else:
        LeftPageList = range(2, current_page)
        LeftMoreTag = False

    return LeftPageList, LeftMoreTag
    
    ##perfectly
    #elif len(range(2, current_page)) == limit_page:
    #    LeftPageList = range(2, current_page)
    #    MoreTag = False
    ##just 2
    #elif len(range(2, current_page)) == 0:
    #    LeftPageList = []
    #    MoreTag = False
    #else:
    #    LeftPageList = range(2, current_page)
    #    MoreTag = False
    

#return right page list
#def get_right(current_page, limit_page):
#
#    return LeftPageList








@register.filter
def rtype(value):
    return type(value)


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

