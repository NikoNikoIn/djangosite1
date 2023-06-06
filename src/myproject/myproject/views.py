from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
    qs = BlogPost.objects.all()[:5]
    context = {"title": "Welcome to My Blog!","blog_list": qs}
    return render(request, "home.html", context)


def about_page(request):
    my_title = "About us"
    return render(request, "about.html", {"title": my_title})


def contact_page(request):
    my_title = "Contact us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    return render(request, "contact.html", {"title": my_title, "form": form})


def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))