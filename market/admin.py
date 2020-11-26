from django.contrib import admin

# Register your models here.
from market.models import Market, Comment, Photo

# admin.site.register(Board)
admin.site.register(Comment)


class PhotoInline(admin.TabularInline):
    model = Photo

class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]
admin.site.register(Market, PostAdmin)