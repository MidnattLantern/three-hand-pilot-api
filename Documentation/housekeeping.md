Pagination
---
Flynarc use pagination to chunk down each item. This means that the frontend app will have to use an infinite scroll component. This extra hassle make Flynarc future proof.
1. In settings.py update REST_FRAMEWORK to this, and pick any number for PAGE_SIZE:
`
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    'DATETIME_FORMAT': '%d %b %Y',
}
`
The datetime format make the date more user friendly

JSON only for end user
---
The interface isn't neccessary for the end user. To disable the html and gizmos, add the following to settins.py above the JWT_AUTH/ REST_USE_JWT group:
`
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
`
