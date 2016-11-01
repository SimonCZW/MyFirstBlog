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

    total_length = int(paginator.num_pages)
    limit_left_length = 2
    limit_right_length = 3
    #get left directory list
    try:
        context['left_pages'], context['LeftMoreTag'] = get_left(int(page), limit_left_length)
    #for index.html without page
    except:
        context['left_pages'], context['LeftMoreTag'] = get_left(1, limit_left_length)

    #get right directory list
    try:
        context['right_pages'], context['RightMoreTag'] = get_right(int(page), limit_right_length, total_length)
    except Exception,e:
#        context['errmsg'] = e
        context['right_pages'], context['RightMoreTag'] = get_right(1, limit_right_length, total_length)

    return ''

#return left page list
def get_left(current_page, limit_list_page):

    #further more
    if len(range(2, current_page)) > limit_list_page:
        LeftPageList = range(2, current_page+1)[-1-limit_list_page:-1]
        LeftMoreTag = True
    #just left directory
    else:
        LeftPageList = range(2, current_page)
        LeftMoreTag = False

    return LeftPageList, LeftMoreTag

def get_right(current_page, limit_list_page, total_list_page):

    if len(range(current_page+1, total_list_page)) > limit_list_page:
        RightPageList = range(current_page+1, total_list_page)[0:limit_list_page]
        RightMoreTag = True

    else:
        RightPageList = range(current_page+1, total_list_page)
        RightMoreTag = False

    return RightPageList, RightMoreTag



###################Learn Custom Template filter/tags#####################
@register.filter
def rtype(value):
    return type(value)
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

