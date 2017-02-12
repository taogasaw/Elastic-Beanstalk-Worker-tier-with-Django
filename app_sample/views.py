from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging


@csrf_exempt  # csrf対策無効化
def put_log(request):
    logging.basicConfig(level=logging.INFO)
    logging.info('Log put!')
    return HttpResponse(status=200)


def root(request):
    return HttpResponse(status=200)
