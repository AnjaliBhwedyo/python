from django.urls import path
from django.contrib import admin
from  . import views 

urlpatterns = [
    path('test/test/',views.test,name="home"),
    path('admin/', admin.site.urls),
    ]