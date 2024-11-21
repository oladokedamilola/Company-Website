# core/views.py

from django.shortcuts import render
from .models import *
from core.forms import ContactForm

def home(request):
    services = Service.objects.all()  # Fetch all services from the database
    contact_form = ContactForm()  # Initialize the contact form
    success = False  # Track if the form was submitted successfully

    if request.method == 'POST':  # Check if the form is submitted
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()  # Save the contact message to the database
            success = True
            contact_form = ContactForm()  # Reset the form after submission

    context = {
        'services': services,         # Pass services to the template
        'contact_form': contact_form,  # Pass the form to the template
        'success': success,            # Pass success message flag to the template
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def resources(request):
    return render(request, 'core/resources.html')

def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'core/terms_of_service.html')

# views.py
# core/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact data to the database
            return render(request, 'core/contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})



# views.py
from django.http import JsonResponse
def blogs(request):
    blogs = Blog.objects.order_by('-created_at')
    print(blogs)  # Check in your server logs
    return render(request, 'core/blogs.html', {'blogs': blogs})



# core/views.py
from django.shortcuts import render, get_object_or_404
from core.models import Blog

def blog_detail(request, slug):
    # Fetch the blog post by its slug
    blog = get_object_or_404(Blog, slug=slug)
    
    # Render the blog details page
    return render(request, 'core/blog_detail.html', {'blog': blog})

