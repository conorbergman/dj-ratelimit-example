from django.http import HttpResponse
from dj_ratelimit import ratelimit
from rest_framework.views import APIView


def basic_key(request):
    return "test"


class IndexView(APIView):
    @ratelimit(rate="1/m", burst_limit=2, key_fn=basic_key)
    def get(self, request=None):
        return HttpResponse("Hello, world.")
