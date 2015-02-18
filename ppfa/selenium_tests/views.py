import datetime
from django.template.context import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404, \
                             redirect, render
from django.utils.safestring import SafeString
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset

from forms import *

from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher

def dologin(request):
    """
    """
    next = None
    if ('next' in request.GET):
        next = request.GET['next']
    if (request.user.is_authenticated()):
        return redirect('/')
    
    form_values = request.POST
    if request.method == 'POST':
        user = authenticate(username=request.POST['Email'].strip(), password=request.POST['Password'].strip())
        try:
            profile = Profile.objects.get(user=user)
            
            if user and user.is_active and profile.Approved == 1:
                login(request, user)
                
                if ('next' in request.GET):
                    return redirect(request.GET['next'])
                else:
                    return redirect('/')
        except:
            pass
             
        form = LoginForm()
        form._errors = ErrorList(['Invalid Email or Password.'])
        return render_to_response('login.html', {'form': form,
                                                        'form_values':form_values,
                                                        'next': next}, 
        context_instance=RequestContext(request))
                    
        
    else:
        form = LoginForm()
        return render_to_response('login.html', {'form': form,
                                                        'form_values':form_values,
                                                        'next': next}, 
        context_instance=RequestContext(request))

def forgot_password(request):
    if request.method == 'POST':
        return password_reset(request, 
            from_email=request.POST.get('email'))
    else:
        return render(request, 'forgot_password.html')

def signup(request):
    """
    """
    next = None
    message = None
    if ('next' in request.GET):
        next = request.GET['next']
    
    form_values = request.POST
    if request.method == 'POST':
        form = SignupForm(request.POST)

        try:
            if form.is_valid():
                form.save()
                user = authenticate(username=request.POST['Email'].strip(), password=request.POST['Password'].strip())
                profile = Profile.objects.get(user=user)
                
                if user and profile.Approved == 1:
                    login(request, user)
                    if ('next' in request.GET):
                        return redirect(request.GET['next'])
                    else:
                        return redirect('/')
                else:
                    return redirect('/pending')
        except:
            form._errors = ErrorList(['Sorry, this email is already in use, please try another.'])
            pass
            
        return render_to_response('signup.html', 
                                {'form': form,
                                'form_values':form_values,
                                'next':next}, 
        context_instance=RequestContext(request))
    else:
        form = SignupForm()
        return render_to_response('signup.html', 
                                {'form': form,
                                'form_values':form_values,
                                'next':next}, 
        context_instance=RequestContext(request))

def pending(request):
    """
    Acceptance Waiting Room
    """
    return render_to_response('pending.html', 
        context_instance=RequestContext(request))
        
@login_required
def home(request):
    """
    page index
    """
    response_dict = {
        'ember_app_name': settings.EMBER_APP_NAME,
        'ember_env': SafeString(settings.EMBER_ENV),
    }
    
    #redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
    #redis_publisher.publish_message(RedisMessage('Snarkie!'))
    
    return render_to_response('home.html', { 'settings': response_dict }, 
            context_instance=RequestContext(request))

def test(request):
    """
    page index
    """
    
    #redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
    #redis_publisher.publish_message(RedisMessage('Snarkie @ '+ str(datetime.datetime.now()) + '!'))
    
    response_dict = {
        'ember_app_name': settings.EMBER_APP_NAME,
        'ember_env': SafeString(settings.EMBER_ENV),
    }
    return render_to_response('test.html', { 'settings': response_dict }, 
            context_instance=RequestContext(request))
