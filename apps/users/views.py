import json
import datetime
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import UserProfile,Banner
from .forms import LoginForm, RegisterForm, UploadImageForm, ModifyPwdForm, UserInfoForm
from utils.mixin_utils import LoginRequiredMixin
from operation.models import UserCourse, UserFavorite, UserMessage
from organization.models import CourseOrg,Teacher
from courses.models import Course



class CustomBackend(ModelBackend):
    """
    实现用户名邮箱均可登录
    继承ModelBackend类，因为它有方法authenticate，可点进源码查看
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        #完成自己的自定义登录逻辑
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):

    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)  # 预加载进行校验
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form": login_form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        # 完成重定向URL
        return HttpResponseRedirect(reverse('index'))


class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("mobile", "")
            if UserProfile.objects.filter(mobile=user_name):
                return render(request, "register.html", {"register_form":register_form, "msg": "用户已经存在"})
            password = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.mobile = user_name
            user_profile.password = make_password(password)
            user_profile.save()

            # 写入欢迎注册消息
            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message = "欢迎注册百世利教育在线网"
            user_message.save()
            return render(request, "login.html")
        else:
            return render(request,"register.html", {"register_form": register_form})


class ForgetPwdView(View):

    def get(self, request):
        return render(request, "forgetpwd.html")


# 用户个人信息
class UserInfoView(LoginRequiredMixin,View):

    def get(self, request):
        return render(request, 'usercenter-info.html',{

        })

    def post(self, request):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')


# 用户修改头像
class UploadImageView(LoginRequiredMixin, View):

    def post(self, request):
        #取用户头像
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            #image = image_form.cleaned_data['image']
            #request.user.image = image
            #request.user.save()
            image_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')


# 个人中心密码修改
class UpdatePwdView(View):

    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            if pwd1!=pwd2:
                return HttpResponse('{"status":"fail", "msg": "密码不一致"}', content_type='application/json')
            user = request.user
            user.password = make_password(pwd2)
            user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(modify_form.errors), content_type='application/json')


# 个人中心 我的课程
class MyCourseView(LoginRequiredMixin,View):

    def get(self, request):

        user_courses = UserCourse.objects.filter(user=request.user)

        return render(request, 'usercenter-mycourse.html',{
            "user_courses": user_courses
        })


# 个人中心 我的收藏 课程机构
class MyFavOrgView(LoginRequiredMixin,View):

    def get(self, request):
        org_list = []
        fav_orgs = UserFavorite.objects.filter(user=request.user, fav_type=2)
        for fav_org in fav_orgs:
            org_id = fav_org.fav_id
            org = CourseOrg.objects.get(id=org_id)
            org_list.append(org)
        return render(request, 'usercenter-fav-org.html', {
            "org_list": org_list
        })


# 个人中心 我的收藏 讲师
class MyFavTeacherView(LoginRequiredMixin,View):

    def get(self, request):
        teacher_list = []
        fav_teachers = UserFavorite.objects.filter(user=request.user, fav_type=3)
        for fav_teacher in fav_teachers:
            teacher_id = fav_teacher.fav_id
            teacher = Teacher.objects.get(id=teacher_id)
            teacher_list.append(teacher)
        return render(request, 'usercenter-fav-teacher.html', {
            "teacher_list": teacher_list
        })


# 个人中心 我的收藏 课程
class MyFavCourseView(LoginRequiredMixin,View):

    def get(self, request):
        course_list = []
        fav_courses = UserFavorite.objects.filter(user=request.user, fav_type=1)
        for fav_course in fav_courses:
            course_id = fav_course.fav_id
            course = Course.objects.get(id=course_id)
            course_list.append(course)
        return render(request, 'usercenter-fav-course.html', {
            "course_list": course_list
        })


# 个人中心 我的消息
class MyMessageView(LoginRequiredMixin,View):

    def get(self, request):
        # 用户进入个人消息后，清空消息记录
        all_message = UserMessage.objects.filter(user=request.user.id)
        all_unread_messages = UserMessage.objects.filter(user=request.user.id, has_read=False)
        for all_unread_message in all_unread_messages:
            all_unread_message.has_read = True
            all_unread_message.save()
        # 对个人消息分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_message, 10, request=request)
        messages = p.page(page)
        return render(request,'usercenter-message.html', {
            "messages": messages
        })


# 首页
class IndexView(View):

    def get(self, request):
        # 获取轮播图
        all_banners = Banner.objects.all().order_by('index')
        courses = Course.objects.filter()[:6]
        banner_courses = Course.objects.filter(is_banner=True)[:3]
        course_orgs = CourseOrg.objects.all()[:15]
        return render(request, "index.html",{
            "all_banners": all_banners,
            "courses": courses,
            "banner_courses": banner_courses,
            "course_orgs": course_orgs
        })










