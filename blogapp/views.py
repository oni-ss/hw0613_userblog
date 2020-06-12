from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import BlogPost
from django.core.paginator import Paginator

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def read(request):
    blogr = Blog.objects.all()
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog.html', {'blogr':blogr, 'posts':posts})

### forms.py 이용X
def create(request):
    if request.method == 'POST':
        blog = Blog()
        blog.image = request.FILES['p']
        blog.title = request.POST['t']
        blog.body = request.POST['b']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('home')
    else:
        return render(request, 'new.html')

def delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')

def update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.title = request.POST['t']
        blog.image = request.FILES['p']
        blog.body = request.POST['b']
        blog.save()
        return redirect('home')
    return render(request, 'update.html', {'blog':blog})

def detail(request, pk):
    blogdet = get_object_or_404(Blog, pk=pk)
    return render(request, 'detail.html', {'blogdet':blogdet})


### forms.py 이용 
def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request,'formnew.html',{'form':form})
