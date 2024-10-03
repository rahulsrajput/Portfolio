from django.shortcuts import render, get_object_or_404
from .models import Contact, Project, Blog, Category, Home, WorkExperience, Education, Certification
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    object = get_object_or_404(Home, pk=1)
    context = {'object':object}
    return render(request, 'app/Home.html', context)


def contact(request):
    contacts = Contact.objects.all()
    context = {'contacts':contacts}
    return render(request, 'app/Contact.html', context)




def blog(request):
    blog_list = Blog.objects.all().order_by('-datePublished')
    paginator = Paginator(blog_list, 5)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    
    
    if request.GET.get('category'):
        query = request.GET.get('category')
        category = Category.objects.get(name=query)
        blogs = Blog.objects.filter(category=category).order_by('-datePublished')
    

    categories = Category.objects.all()
    context = {'blogs':blogs, 'categories':categories}
    return render(request, 'app/Blog.html', context)


def blogDetail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    context = {'blog':blog}
    return render(request, 'app/BlogDetail.html', context)




def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'app/Projects.html', context)


def resume(request):
    works = WorkExperience.objects.all()
    edus = Education.objects.all()
    certificates = Certification.objects.all()
    context = {'works':works, 'edus':edus, 'certificates':certificates}
    return render(request, 'app/Resume.html', context)