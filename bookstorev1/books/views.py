import datetime

from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.


html = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    background-color: lightblue;
}

h1 {
    color: white;
    text-align: center;
}

p {
    font-family: verdana;
    font-size: 20px;
}
</style>
</head>
<body>

<h1>%s</h1>
<p>%s</p>

</body>
</html>
"""

def index(request):
    #return HttpResponse(html%('Welcome...', 'First page work in progresss..'))
    now = datetime.datetime.now()
    context = {'page_title': 'Current date time',
                'current_time': now,
                'page_heading': 'Django Time'
                }
    return render(request, 'books/index.html', context)
    

def current_datetime(request):
    """
    now = datetime.datetime.now()
    html = "<html><body>It is now <em>{}</em>.</body></html>".format(now)        
    return HttpResponse(html)
    """
    now = datetime.datetime.now()
    context = {'page_title': 'Current date time',
                'current_time': now
                }
    return render(request, 'books/time.html', context)

def hours_delta(request, offset=1):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    data = "In %s hour(s), it will be  %s." % (offset, dt)

    return HttpResponse(html%('Time Delta', data))

def profile(request):
    context = {
        'title': 'Profile Page',
        'heading': 'Profile'
    }

    if not request.user.is_authenticated:
        context['heading'] = 'Must authenticate...'
        context['content'] = 'Must <a href="/login/">login</a> to view your profile.'
    
    return render(request, 'books/profile.html', context)

def login_view(request):
    context = {
        'page_title': 'Login',
        'heading': 'Login',
        'content': "<h1>Some content</h1> <script>alert('hello')</script>"
    }
    return render(request, 'books/login.html', context)


def loginProcess(request):
    errors = []
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if not username:
            errors.append('Username is required')
        if not password:
            errors.append('Password is required')

        if not errors:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user) #adds session info for user
                    #return profile(request)
                    return HttpResponseRedirect(
                            reverse('profile'))
                else:
                    errors.append('This account has been disabled.')
            else:
                errors.append('Invalid username or password.')

        context['errors'] = errors
        return render(request, 'books/login.html', context)
    else:
        login_view(request)


def logout_view(request):
    logout(request)
    context = {
        'heading': 'Successfully logged out.',
        'content': 'Log back in again.',
        'page_title': 'Logout Successful'
    }
    return render(request, 'books/login.html', context)