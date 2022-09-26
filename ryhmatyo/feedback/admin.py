from django.contrib import admin
from .models import Topic, Feedback
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields=['name']
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('topic','rating','good','bad','ideas','date')
    list_filter=['topic','date']
    search_fields=['good','bad']

# Register your models here.
admin.site.register(Topic,TopicAdmin)
admin.site.register(Feedback,FeedbackAdmin)
