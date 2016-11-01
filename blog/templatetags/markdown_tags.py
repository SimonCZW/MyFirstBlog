from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.utils.html import format_html
import markdown

register = template.Library()

#markdown filter
@register.filter(needs_autoescape=True)
@stringfilter
def Trans4markdown(value, autoescape=True):
     return format_html(markdown.markdown(force_text(value)))
#     return mark_safe(markdown.markdown(force_text(value),
#         extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables", "spoiler"]))


#testing custom tag with markdown
@register.tag
def markdown_tag(parser, token):
    nodelist = parser.parse(('endmarkdown_tag',))
    parser.delete_first_token()
    return MarkdownNode(nodelist)
class MarkdownNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        output = self.nodelist.render(context)
        return markdown(output)
