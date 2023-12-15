from django.contrib import admin
from webapp.models import Task, Status, Type


admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'created_at']
    list_display_links = ['id', 'summary']
    list_filter = ['status']
    search_fields = ['summary', 'description']
    fields = ['summary', 'author', 'description', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']