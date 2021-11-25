from django.http import HttpResponse

def index(requiest):
    return HttpResponse('hello world. your\'re at the polls index.')

