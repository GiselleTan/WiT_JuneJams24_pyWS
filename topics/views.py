from django.shortcuts import render
from topics.models import Topic

def topic_index(request):
    topics = Topic.objects.all()
    context = {
        "topics": topics
    }
    return render(request, "topics/topic_index.html", context)

def topic_detail(request, pk):
    topic = Topic.objects.get(pk=pk)
    context = {
        "topic": topic
    }
    return render(request, "topics/topic_detail.html", context)
