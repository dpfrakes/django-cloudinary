# Django Cloudinary

Django app to list, upload, and edit Cloudinary resources via the web admin.

### Installation

```
pip install -e git://github.com/dpfrakes/django-cloudinary.git#egg=django-cloudinary
```

Add the following to your Django settings file:

```
INSTALLED_APPS = (
    ...
    'django_cloudinary',
   )
```

Additionally, add `CLOUDINARY` settings:

```
CLOUDINARY = {
    'cloud_name': env('CLOUDINARY_CLOUD_NAME', default='abcdefghi'),
    'api_key': env('CLOUDINARY_API_KEY', default='123456789012345'),
    'api_secret': env('CLOUDINARY_API_SECRET', default='111111111111111111111111111'),
    'upload_preset': env('CLOUDINARY_UPLOAD_PRESET', default='abcdefgh')
}
```

Add a link to your Django admin dashboard to `'/admin/cloudinary'`.