from django.shortcuts import render

def home(request):
    """Home page view"""
    context = {
        'title': 'Welcome to your website!',
        'message': 'This is your first page created with Django and Docker',
    }
    return render(request, 'home.html', context)

def template1(request):
    """Template 1 view"""
    context = {
        'title': 'Template 1',
        'description': 'First example page',
        'content': 'Here you can add your content...',
    }
    return render(request, 'template1.html', context)

def template2(request):
    """Template 2 view"""
    context = {
        'title': 'Template 2',
        'description': 'Second example page',
        'content': 'Here you can add your content...',
    }
    return render(request, 'template2.html', context)

def template3(request):
    """Template 3 view"""
    context = {
        'title': 'Template 3',
        'description': 'Third example page',
        'content': 'Here you can add your content...',
    }
    return render(request, 'template3.html', context)

def template4(request):
    """Template 4 view"""
    context = {
        'title': 'Template 4',
        'description': 'Fourth example page',
        'content': 'Here you can add your content...',
    }
    return render(request, 'template4.html', context)