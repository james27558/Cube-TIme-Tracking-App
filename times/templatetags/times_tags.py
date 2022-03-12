from django import template

register = template.Library()

@register.filter(name="getTag")
def getTag(value, index):
    tags = value[index]
    if len(tags) == 1:
        return tags[0]
    else:
        return ", ".join(tags)
