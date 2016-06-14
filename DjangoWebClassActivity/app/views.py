"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import render_to_response
from app.models import Activity, User, JOINT_ACTIVITY
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    activities = Activity.objects.all()
    page = {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    return render(
        request,
        'app/index.html',
        locals()
    )
    
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def mylist(request):
    """Renders the about page."""
    if not request.user.is_authenticated():
        return HttpResponseRedirect('login')
    assert isinstance(request, HttpRequest)
    page = {
            'title':'參加的活動列表',
            'year':datetime.now().year,
        }
    jointact = JOINT_ACTIVITY.objects.filter(user_id = request.user.username)
    if jointact:
        activities = Activity.objects.filter(id = jointact[0].act_id)

    return render(
        request,
        'app/about.html',
        locals()
    )

def releaselist(request):
    """Renders the about page."""
    if not request.user.is_authenticated():
        return HttpResponseRedirect('login')
    assert isinstance(request, HttpRequest)
    page = {
            'title':'發佈的活動列表',
            'year':datetime.now().year,
        }
    activities = Activity.objects.filter(author = request.user.username)
    return render(
        request,
        'app/about.html',
        locals()
    )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()
    
    page = {
            'title':'註冊',
            'year':datetime.now().year,
        }    

    return render(
        request,
        'app/register.html',
        locals()
    )

def publish(request):
    return False

def apply(request):
    if request.method == 'GET':
        activity_id = request.GET['act_id']
        JOINT_ACTIVITY.objects.create(
           user_id = request.user.username,
           act_id = activity_id,
        )
    return HttpResponseRedirect('/mylist/')