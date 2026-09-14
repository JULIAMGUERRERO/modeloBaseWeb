from django.shortcuts import render

def home(request):
    """Home page view"""
    context = {
        'titulo': 'Welcome to your website!',
        'mensaje': 'This is your first page created with Django and Docker',
    }
    return render(request, 'home.html', context)

def template1(request):
    """Template 1 view"""
    context = {
        'titulo': 'Template 1',
        'descripcion': 'First example page',
        'content': 'Here you can add your content...',
    }
    return render(request, 'template1.html', context)

def template2(request):
    """Template 2 view"""
    context = {
        'titulo': 'Template 2',
        'descripcion': 'Second example page',
        'content': 'Here you can add your content...',
    }
    return render(request, 'template2.html', context)

def template3(request):
    """Template 3 view"""
    context = {
        'titulo': 'Template 3',
        'descripcion': 'Third example page',
        'content': 'Here you can add your content...',
    }
    return render(request, 'template3.html', context)

def template4(request):
    """Template 4 view"""
    context = {
        'titulo': 'Template 4',
        'descripcion': 'Fourth example page',
        'content': 'Here you can add your content...',
    }
    return render(request, 'template4.html', context)