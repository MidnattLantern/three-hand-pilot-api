https://docs.google.com/document/d/1v8mOyB5l7aSL5loy3MVIX4z4SsLYKe-ZEGGpT_Z5DRM/edit

Flynarc API use json webtokens for enhanced security.
1. Flynarc API use a long term supported version of dj-rest-auth. In terminal, run:
- `pip3 install dj-rest-auth==2.1.9`

2. Add to installed apps:
- `'rest_framework.authtoken',`
- `'dj_rest_auth',`

3. Add to head urls.py underneath the "api-auth" route:
`path('dj-rest-auth/', include('dj_rest_auth.urls')),`

4. Make migrations/ Migrate

5. Allauth allow the user to sign-up from the front-end.
Run in terminal:
- `pip3 install 'dj-rest-auth[with_social]'`

6. Add the following to installed apps underneath `dj_rest_auth`:
- `'django.contrib.sites',`
- `'allauth',`
- `'allauth.account',`
- `'allauth.socialaccount',`
- `'dj_rest_auth.registration',`

7. Set SITE_ID = 1, it should be found below installed apps

8. Add the path in the head urls.py
- `path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),`

9. Run in terminal:
- `pip3 install djangorestframework-simplejwt`

Add this block underneath `BASE_DIR = Path(__file__).resolve().parent.parent`:
`
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )]
}

REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refrest-token'
`
serializers.py in flynarc_api
---
The serializer.py file among things, let the front-end display the authenticated user information and unlock content.
1. Create the serializers.py file inside flynarc_api

2. Paste the following code to serializers.py
`
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """ Docstring """
    user_authentication_id = serializers.ReadOnlyField(source='profile.id')
    user_authentication_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'user_authentication_id', 'user_authentication_image'
        )

`

3. In settings.py, Add the block underneath the JWT_AUTH group:
`
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'flynarc_api.serializers.CurrentUserSerializer'
}
`

4. Makemigrations/ migrate

JSON webtoken setup should be finished here.