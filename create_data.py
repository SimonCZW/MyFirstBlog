#!/usr/local/python

from myblog.wsgi import *
from blog.models import Category,Paper

CategoryList = ['opendaylight', 'netconf', 'sdn']

for category in CategoryList:
    c = Category.objects.get_or_create(name=category)[0]
    for i in range(1,6):
        p = Paper.objects.get_or_create(
            title = category+'_'+str(i),
            content = "This is a test...",
            author = "SimonCZW"
        )[0]
        p.category.add(c)

print "Done!"




