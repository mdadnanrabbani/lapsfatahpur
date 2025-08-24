from django.contrib import admin
from home.models import contactFrom
from .models import Notice



# Register your models here.
admin.site.register(contactFrom)


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created_at')
    search_fields = ('subject', 'content')
    list_filter = ('created_at',)
