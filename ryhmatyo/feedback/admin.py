from django.contrib import admin
from .models import Topic, Feedback
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields=['name']
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('rating','good','bad','date')
    list_filter=['topic','date']
    search_fields=['good','bad']

# Register your models here.
admin.site.register(Topic)
admin.site.register(Feedback,FeedbackAdmin)
