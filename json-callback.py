from django.http import HttpResponse
import simplejson

def jsonResponse(request, response_data):
    try:
        func = request.GET.get('callback')
        return HttpResponse(func + '(' + simplejson.dumps(response_data) + ')', mimetype="application/javascript")
    except:
        return HttpResponse(simplejson.dumps(response_data), mimetype="application/javascript")
