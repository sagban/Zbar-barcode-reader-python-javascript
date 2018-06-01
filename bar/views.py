from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt

from . import barCode
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from datetime import datetime, timedelta, date
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.




@csrf_exempt
def decodeAjax(request):

    if request.POST:
        decodedData = barCode.decode(request.POST['imgBase64'])
        if decodedData:
            return JsonResponse({"code" : decodedData})
        return JsonResponse({"code" : 'NO BarCode Found'})


#@static_vars(i=0)
def ScanBooks(request):
    return render(request, "ScanBook.html")

