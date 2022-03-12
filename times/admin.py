from django.contrib import admin
from .models import Session, Attempt, Cube, Tag, EventType

# Register your models here.
admin.site.register(Session)
admin.site.register(Attempt)
admin.site.register(Cube)
admin.site.register(Tag)
admin.site.register(EventType)

