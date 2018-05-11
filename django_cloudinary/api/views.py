from urllib import parse

from cloudinary.utils import api_sign_request
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(('GET',))
def sign_cloudinary_request(request):
    param_keys = request.GET
    sign_params = {}
    for key in param_keys:
        sign_params.update({key: param_keys[key]})
    signature = api_sign_request(sign_params, api_secret=settings.CLOUDINARY['api_secret'])
    return JsonResponse({'signature': signature})
