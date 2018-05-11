from django.conf.urls import url

from .views import CloudinaryUploaderView, CloudinaryListView, menu, editor

urlpatterns = [
    url(r'^$', menu, name='cloudinary_menu'),
    url(r'^upload', CloudinaryUploaderView.as_view(), name='cloudinary_upload'),
    url(r'^list', CloudinaryListView.as_view(), name='cloudinary_list'),
    url(r'^editor/(?P<public_id>.+)', editor, name='cloudinary_editor'),
]
