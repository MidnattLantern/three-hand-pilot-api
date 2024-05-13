Run in terminal:
- `pip3 install djangorestframework`
In settings.py add to installed apps underneath `'cloudinary',`:
`'rest_framework',`
Clear views.py and import:
- `from rest_framework.views import APIView`
- `from rest_framework.response import Response`