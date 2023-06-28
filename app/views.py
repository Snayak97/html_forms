from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *


#normal checking purpose

def first(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        
        return HttpResponse('inserted data')


    return render(request,'first.html')


#inserted data

def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Topic is inserted')
    
    return render(request,'insert_topic.html')

def insert_webpage(request):
    if request.method=='POST':
        topic=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()

        name=request.POST['name']
        url=request.POST['url']
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        
        return HttpResponse('inserted Webpages')

    return render(request,'insert_webpage.html')

def insert_Acess(request):
    if request.method=='POST':
        topic=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()

        name=request.POST['name']
        url=request.POST['url']
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()

        date=request.POST['date']
        author=request.POST['author']
        AO=AcessRecord.objects.get_or_create(name=WO,date=date,author=author)[0]
        AO.save()

        
        return HttpResponse('inserted AcessRecord')

    return render(request,'insert_Acess.html')






#display webpages
def display_webpage(request):
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpage.html',d)

#display webpages
def display_Acess(request):
    Acess=AcessRecord.objects.all()
    d={'Acess':Acess}
    return render(request,'display_Acess.html',d)
