from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
# Create your views here.
def new(request):
    return render(request, 'new.html')

def post(request):
    blogs = Blog.objects.all()

    return render(request, 'post.html', {'blogs': blogs})

def detail(request, post_id):
    blog = get_object_or_404(Blog, pk=post_id)
    return render(request, 'detail.html', {'blog': blog})

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.startdate = request.POST['startdate']
    blog.returndate = request.POST['returndate']
    blog.location = request.POST['location']
    blog.cartype = request.POST['cartype']
    blog.body = request.POST['body']
   
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/post/')
