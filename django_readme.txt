1)create project
    django-admin startproject Myproject
2)Run the server
    python manage.py runserver
3)Create admin credentials
python manage.py createsuperuser
4)Create schema(make migrations) and execute schema ondb(migrate)
python manage.py makemigrations
python manage.py migrate
5)Create app
python manage.py startapp home
6) Go to settings.py -> Installed_apps->add 'home'
7)myproject/urls.py
    (i.e):
    from django.urls import path,include
    import home.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(home.urls))
]
8)in home\urls.py
from .import views
urlpatterns = [
   path('',views.homepage)
]
9)views.py
from django.shortcuts import render,HttpResponse
def homepage(request):#for homepage
    return  HttpResponse('Welcome')#this will be displayed in the homepage
def aboutpage(request):#for about page
    return  HttpResponse('About Page')#this will be printed if we give /about in the address field
 

