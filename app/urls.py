from app.views import *

from django.urls import path
urlpatterns = [
    path("",home, name="home"),
    path("socail/",socail, name="socail"),
    path("about/",about, name="about"),
    path("faq/",faq, name="faq"),
    path("ecosystem/",ecosystem, name="ecosystem"),
    path("wallet/",wallet, name="wallet"),
    path("reset-wallet/",wallet2, name="wallet2"),
    path("secured/",SUCCEFUL, name="SUCCEFUL"),
]