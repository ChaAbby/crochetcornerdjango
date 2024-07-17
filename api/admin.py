from django.contrib import admin

# Register your models here.
from .models import Post, Image, Pattern, Inspiration, Tool, Yarn

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Pattern)
admin.site.register(Inspiration)
admin.site.register(Tool)
admin.site.register(Yarn)