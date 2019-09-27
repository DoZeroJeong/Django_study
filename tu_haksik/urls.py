from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('community/', include('community.urls')),
    path('accounts/', include('accounts.urls')),
    path('dormitory/', include('dormitory.urls')),
    path('restaurant/', include('restaurant.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/doc/', get_swagger_view(title='Haksik_API Manual')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
