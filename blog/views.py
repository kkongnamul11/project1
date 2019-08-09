from django.shortcuts import render
from django.http import HttpResponse
from .models import blog, imageMain
# Create your views here.


def index(request):
    #return HttpResponse('HELLO FORM POSTS')
    blogs = blog.objects.all()[:10]
    mainbanner = imageMain.objects.all()
    context = {
        'title' : "Latest Title",
        'blogs' : blogs,
        'mainbanner' : mainbanner,
    }
        
    return render(request, 'blog/index.html', context)
    
    
def details(request, id):
    mblog = blog.objects.get(id=id)

    context = {
        'blog' : mblog
    }

    return render(request, 'blog/details.html', context)
