from django.contrib import admin
from django.urls import path
from core.views import base, login, signin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base),
    path('login/', login),
    path('signin/', signin)
]
