from django.urls import path
from . import views

urlpatterns=[
	# path('',views.myfun),
     # path('xyz/',views.example),
	path('',views.index),
	path('about/',views.about),
	path('contact/',views.contact),
	path('services/',views.service),
	path('register/',views.register),
	path('login/',views.login),
	path('logout/',views.logout),
	path('display/',views.display),
    path('update/',views.update),
    path('delete/',views.delete)
]