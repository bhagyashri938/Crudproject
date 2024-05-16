from django.urls import path
from myapp import views
urlpatterns=[
    path("",views.display,name='display'),
    path("create/",views.add,name='add'),
]