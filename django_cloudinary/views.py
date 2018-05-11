from urllib import parse

import cloudinary
from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView

from .util import get_api_usage_info


class CloudinaryUploaderView(TemplateView):
    """
    Render the Cloudinary upload widget
    """
    template_name = 'upload_widget.html'

    def get_context_data(self, **kwargs):
        context = super(CloudinaryUploaderView, self).get_context_data(**kwargs)
        response = cloudinary.api.root_folders()
        context.update({
            'cloud_name': settings.CLOUDINARY['cloud_name'],
            'api_key': settings.CLOUDINARY['api_key'],
            'cloudinary_folders': response['folders'],
            'upload_preset': settings.CLOUDINARY['upload_preset'],
            'dropbox_app_key': settings.DROPBOX_APP_KEY
        })
        return context


class CloudinaryListView(TemplateView):
    """
    List all resources uploaded to Cloudinary
    """
    template_name = 'resource_list.html'

    def get_context_data(self, **kwargs):
        context = super(CloudinaryListView, self).get_context_data(**kwargs)
        cloudinary.config(
            cloud_name=settings.CLOUDINARY['cloud_name'],
            api_key=settings.CLOUDINARY['api_key'],
            api_secret=settings.CLOUDINARY['api_secret'],
        )
        response = cloudinary.api.resources(max_results=50)
        resources = response['resources']

        for resource in resources:
            url = resource['secure_url']
            path = url.split('/')
            path.insert(path.index('upload') + 1, 't_media_lib_thumb')
            resource['thumbnail_url'] = '/'.join(path)

        context['cloudinary_resources'] = response['resources']
        context.update(get_api_usage_info(response))
        return context


def menu(request):
    return render(request, 'menu.html')


def editor(request, public_id):
    response = cloudinary.api.resource(parse.quote(public_id))
    context = {'resource': response}
    context.update(get_api_usage_info(response))
    return render(request, 'image_editor.html', context)
