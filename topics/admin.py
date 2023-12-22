from django.contrib import admin
from topics.models import Topic

class TopicAdmin(admin.ModelAdmin):
    pass

admin.site.register(Topic, TopicAdmin)
