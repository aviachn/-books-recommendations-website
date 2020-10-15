from django.contrib import admin
from .models import Article
# Register your models here.
admin.site.register(Article)       #this is the way we're telling django to register something on the admin site