from django import template

register = template.Library()

@register.filter
def youtube_embed(url):
    if url and "watch?v=" in url:
        return url.replace("watch?v=", "embed/")
    return url