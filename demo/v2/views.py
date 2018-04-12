from django.shortcuts import render, HttpResponse

# Create your views here.

def hello_v2(request, version = "v1"):
	return HttpResponse('base alive hello_v2')
