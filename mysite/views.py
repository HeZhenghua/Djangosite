__author__ = 'Sunsmile'
import  datetime
from django.http import HttpResponse
def hello(request):
    now=datetime.datetime.now()
    htm=r"<html><body><h1>this is %s</h1></body></html>" %(now)
    assert False
    return HttpResponse(htm)