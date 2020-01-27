from django.urls import path, include,re_path

from users.views import UserInfoView, UploadImageView, UpdatePwdView, MyCourseView
from users.views import MyFavOrgView, MyFavTeacherView, MyFavCourseView, MyMessageView
from users.views import LogoutView



app_name = "users"

urlpatterns = [
    # 用户信息
    path('info/', UserInfoView.as_view(), name="user_info"),
    # 用户头像上传
    path('image/upload/', UploadImageView.as_view(), name="image_upload"),
    # 个人中心密码修改
    path('update/pwd/', UpdatePwdView.as_view(), name="update_pwd"),
    # 个人中心 我的课程
    path('mycourse/', MyCourseView.as_view(), name="my_course"),
    # 个人中心 我的收藏 课程机构
    path('myfav/org/', MyFavOrgView.as_view(), name="myfav_org"),
    # 个人中心 我的收藏 讲师
    path('myfav/teacher/', MyFavTeacherView.as_view(), name="myfav_teacher"),
    # 个人中心 我的收藏 课程
    path('myfav/course/', MyFavCourseView.as_view(), name="myfav_course"),
    # 个人中心 我的消息
    path('mymessage/', MyMessageView.as_view(), name="mymessage"),
    # 退出登录
    path('logout/', LogoutView.as_view(), name="logout"),
]