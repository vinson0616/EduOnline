"""EduOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve

from users.views import LoginView, RegisterView, ForgetPwdView, IndexView
from organization.views import OrgView
from EduOnline.settings import MEDIA_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    #path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),

    # 验证码
    path('captcha/', include('captcha.urls')),
    # 忘记密码
    path('forget/', ForgetPwdView.as_view(), name="forget_pwd"),


    # 配置上传文件的访问处理函数
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    # 配置static处理函数
    #re_path('static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),


    # 课程机构 相关url配置
    path("org/", include('organization.urls', namespace="org")),

    #课程 相关url配置
    path("course/", include('courses.urls', namespace="course")),

    # 用户 相关url配置
    path("users/", include('users.urls', namespace="users")),

]


