from multiprocessing import context
from unicodedata import category
from django.shortcuts import get_object_or_404, render
from .models import Category, Blogs
from pages.models import ServicesField

# Create your views here.

def blogs(request):
    blogs = Blogs.objects.all()
    category = Category.objects.all()
    services = ServicesField.objects.all()

    context = {
        'category' : category,
        'blogs' : blogs,
        'services' : services
    }
    return render(request, 'blog/blogs.html', context)

def blog_detail(request, slug):
    blog = Blogs.objects.get(slug=slug)
    blogs = Blogs.objects.all()
    
    context = {
        'blog' : blog,
        'blogs' : blogs
    }
    return render(request, 'blog/blog_detail.html',context)

    

def blogs_by_category(request, slug):
    context = {
        'blogs' : Blogs.objects.filter(category__slug=slug),
        'category' : Category.objects.all(),
        'selected_category' : slug
    }
    return render(request, "blog/blogs.html", context)