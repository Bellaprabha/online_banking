from django.contrib import admin
from django.urls import path
from accounts import views
# from accounts.views import createAccounts
# from accounts.views import ShowAcntDetails


urlpatterns = [
    
    path('createAc/',views.createAccounts),
    path("showAc/",views.ShowAcntDetails),
  
]