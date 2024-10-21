from django.contrib import admin
from django.urls import path
from core.views import base, login, signin, adminlogin
from testingapp.views import sample 

urlpatterns = [
    path('admin/login/', adminlogin, name='adminlogin'),
    path('admin/', admin.site.urls),
    path('', base),
    path('login/', login),
    path('signin/', signin),
    path('sample/', sample),
    path('#base', base)
]
