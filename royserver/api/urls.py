from django.conf.urls import url, include
from django.urls import path, include, re_path
from . import views


# api url 配置
app_name = 'api'
urlpatterns = [
    path('test/',views.GetMessageView.as_view()),
]
