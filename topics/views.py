from django.shortcuts import render
from topics.models import Topic

topics_dict = {
    "topic1" : {
        "title": 'Hello, World',
        "definition": 'The first thing we will learn is the print statement. The print statement is used to print out a line.'
    },
    "topic2" : {
        "title": 'Variables and Types',
        "definition": 'Variables are used to store data types. A variable can be created simply by assigning it a value.\n Example: x = 5 where x is the variable, containing the value 5, whose data type is an int (short for integer).\n' 
        + 'There are various built-in data types in python such as:\n' 
        + 'str (eg: x = "Hello World"),\n'
        + 'int (eg: x = 5),\n'
        + 'float (eg: x = 5.0),\n'
        + 'list (eg: x = ["apple", "banana", "cherry"]),\n'
        + 'dict (eg: x = {"name" : "John", "age" : 36}),\n'
        + 'bool (eg x = True).'
    },
    "topic3" : {
        "title": 'Lists',
        "definition": 'List can be used to store multiple items. The items in a list are:\n' 
        + 'Changeable - We can add, edit or remove items in a list.\n' 
        + 'Ordered - When a new item is added to the list, it will be placed at the end of the list. The order of the list will not change.\n'
        + 'Allow duplicate values - Items in a list can have the same values.\n'
    },
    "topic4" : {
        "title": 'Basic Operators',
        "definition": ''
    },
    "topic5" : {
        "title": 'String Formatting',
        "definition": ''
    },
    "topic6" : {
        "title": 'Basic String Operations',
        "definition": ''
    },
    "topic7" : {
        "title": 'Conditions',
        "definition": ''
    },
    "topic8" : {
        "title": 'Loops',
        "definition": ''
    },
    "topic9" : {
        "title": 'Functions',
        "definition": ''
    },
}

def reset_topics():
    Topic.objects.all().delete()
    for topic in topics_dict:
        Topic.objects.create(title=topics_dict[topic]["title"], definition=topics_dict[topic]["definition"])

# Uncomment to reset topics stored in database
# reset_topics()

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
