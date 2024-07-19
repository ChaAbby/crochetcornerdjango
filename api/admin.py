from django.contrib import admin

# Register your models here.
from .models import Post, Pattern, Inspiration, Tool, Yarn

admin.site.register(Post)
admin.site.register(Pattern)
admin.site.register(Inspiration)
admin.site.register(Tool)
admin.site.register(Yarn)