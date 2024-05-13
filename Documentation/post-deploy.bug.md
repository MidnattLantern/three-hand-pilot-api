To patch a bug that wasn't addressed, go to views.py inside flynarc_api directory, and import:
`
from .settings import (
    JWT_AUTH_COOKIE,
    JWT_AUTH_REFRESH_COOKIE,
    JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)
`

Then add this block:
`
@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01, Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
`

in urls.py import logout_route with root_route, then add these above `api-auth` route:
`
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
`