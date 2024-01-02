from django.shortcuts import render
from topics.models import Topic

topic_list = ['Hello, World', 'Variables and Types', 'Lists', 'Basic Operators', 'String Formatting', 
              'Basic String Operations', 'Conditions', 'Loops', 'Functions']
for i in range(len(topic_list)):
    Topic.objects.create(title=topic_list[i])

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
