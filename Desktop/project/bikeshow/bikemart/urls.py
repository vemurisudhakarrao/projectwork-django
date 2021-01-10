from django.contrib import admin
from django.urls import path
from bikemart import views
from django.contrib.auth import views as v
urlpatterns = [
path('',views.home,name="hm"),
path('about/',views.about,name="ab"),
path('lt/',views.latest,name="la"),
path('rg/',views.reg,name="rg"),
path('lg/',v.LoginView.as_view(template_name="bmtl/login.html"),name="lg"),
path('lgo/',v.LogoutView.as_view(template_name="bmtl/logout.html"),name="lgg"),
path('bn/',views.booknow,name="bn"),
path('tvs/',views.booktvs,name="tvs"),

]