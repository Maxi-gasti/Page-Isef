from django.urls import path    
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('wiki', views.wiki, name="wiki"),
    path('requeriments', views.requeriments, name="requeriments"),
    path('download', views.download, name="descarga"),
    path('contact',views.contact, name="contact"),
    path('planes', views.plans, name="plans"),
    path('profile', views.profile, name="profile"),
    path('register', views.register, name="registro"),
    path('signin', views.signin, name="signin"),
    path('logout', views.signout, name="logout"),
    path('buy',views.buy, name="buy"),
    path('buyP',views.buyP, name="buyP"),
    path('PlanError',views.errorplan, name="error-plan"),
    path('working',views.work, name="work")
]
