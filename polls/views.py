from django.http import HttpResponse
from django.conf import settings


def index(request):
    return HttpResponse("Random Index Route.")


def derp(request):
    return HttpResponse("Another Derp Derp")


def env_check(request):
    return HttpResponse("TEST_ENV_LARP VALUE: " + settings.TEST_ENV_LARP)