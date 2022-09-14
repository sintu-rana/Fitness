from home.views import index
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path('',views.index,name='home'),
   path('about',views.about,name='about'),
   path('EatBetter',views.EatBetter,name='EatBetter'),
   path('GetFit',views.GetFit,name='GetFit'),
   path('ManageWeight',views.ManageWeight,name='ManageWeight'),
   path('contact',views.contact,name='contacts'),
   path('login',views.loginUser,name='login'),
   path('signup',views.signupUser,name='signup'),
   path('logout',views.logoutUser,name='logout'),
   path('article1',views.article1,name='article1'),
   path('Challenges',views.Challenges,name='Challenges'),
   path('plankchallenge',views.plankchallenge,name='plankchallenge'),
   path('pushupchallenge',views.pushupchallenge,name='pushupchallenge'),
   path('legchallenge',views.legchallenge,name='legchallenge'),
   path('burpeechallenge',views.burpeechallenge,name='burpeechallenge'),
   path('healthtips',views.healthtips,name='healthtips'),
   path('Cooking',views.Cooking,name='Cooking')

]
