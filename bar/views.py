
from django.views.decorators.csrf import csrf_exempt
from . import barCode
from django.shortcuts import render
from django.http import JsonResponse

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

