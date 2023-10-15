from django import template 

register = template.Library()

def google_translate(type="simple",language="en"):
    return {
        "language":language,
        "type":type
    }