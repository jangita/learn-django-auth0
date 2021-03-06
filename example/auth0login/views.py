from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode

from django.contrib.auth import logout as log_out

def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect('/home')
    else:
        return render(request, 'index.html')


def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)