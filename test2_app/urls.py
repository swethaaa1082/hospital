from django.urls import path
from test2_app import views
urlpatterns = [

    path('',views.home,name='home'),

    path('<slug:c_slug>/', views.home, name='doctors_by_department'),
    path('<slug:c_slug>/<slug:doctor_slug>/', views.DoctDetail, name='DoctDetail')

]