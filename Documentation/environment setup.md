First steps
---
Flynarc API use a long term supported version of Django.
1. Run in terminal:
- `pip3 install 'django<4'`
2. To create the Flynarc API project, run in terminal:
- `django-admin startproject flynarc_api .`
3. Create and add to the `env.py` file:
- `DS_Store`
- `env.py`

Image support
---
Cloudinary is a image hosting service. https://cloudinary.com/
The API url can be found inside Dashboard
Flynarc_api use a long term support of Cloudinary.
1. Run in terminal:
- `pip install django-cloudinary-storage==0.3.0`
Pillow is a image proccessing package.
2. Run in terminal:
- `pip install Pillow`
3. Create and add to the env.py file:
- `import os`
- `os.environ['CLOUDINARY_URL'] = 'cloudinary://`(cloudinary api key)`'`
4. Above `BASE_DIR = Path(__file__).resolve().parent.parent`, add:
- `
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
`
- `MEDIA_URL = '/media/'`
- `DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'`
The name for placeholder profile picture is "default_profile_rmkaor"
The name for placeholder picture is "default_post_y8afhe"

settings.py Installed apps
---
1. Add the apps:
- `'cloudinary_storage',`
- `'cloudinary',`
2. The new installed apps block must be in this order:
`
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
]
`

settings.py import env.py
---
1. Underneath `from pathlib import Path`, import:
- `import os`
- `
if os.path.exists('env.py'):
    import env
`