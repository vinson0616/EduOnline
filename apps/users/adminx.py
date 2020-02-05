import xadmin
from xadmin import views

from .models import EmailVerifyCode, Banner,UserProfile
from courses.models import Course, Video, Lesson, CourseResource,BannerCourse
from operation.models import CourseComments, UserFavorite, UserMessage, UserCourse, UserAsk, JifenDetail
from organization.models import CityDict, Teacher, CourseOrg
from django.contrib.auth.models import Group, Permission
from xadmin.models import Log
from order.models import JifenPay


class BaseSetting(object):
    enable_themes = True  #主题开启
    use_bootswatch = True  #主题开启


class GlobalSettings(object):
    site_title = "百世利在线教育管理系统"  #页面左上角
    site_footer = "2020 百世利教育"
    # menu_style = "accordion"

    def get_site_menu(self):
        return (
            {'title': '课程管理', 'menus': (
                {'title': '课程信息', 'url': self.get_model_url(Course, 'changelist')},
                {'title': '轮播课程', 'url': self.get_model_url(BannerCourse, 'changelist')},
                {'title': '章节信息', 'url': self.get_model_url(Lesson, 'changelist')},
                {'title': '视频信息', 'url': self.get_model_url(Video, 'changelist')},
                {'title': '课程资源', 'url': self.get_model_url(CourseResource, 'changelist')},
                {'title': '课程评论', 'url': self.get_model_url(CourseComments, 'changelist')},
            )},
            {'title': '机构管理', 'menus': (
                {'title': '机构信息', 'url': self.get_model_url(CourseOrg, 'changelist')},
                {'title': '机构讲师', 'url': self.get_model_url(Teacher, 'changelist')},
                {'title': '所在城市', 'url': self.get_model_url(CityDict, 'changelist')},
            )},
            {'title': '用户管理', 'menus': (
                {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
                {'title': '积分管理', 'url': self.get_model_url(JifenDetail, 'changelist')},
                {'title': '用户验证', 'url': self.get_model_url(EmailVerifyCode, 'changelist')},
                {'title': '购买课程', 'url': self.get_model_url(UserCourse, 'changelist')},
                {'title': '用户收藏', 'url': self.get_model_url(UserFavorite, 'changelist')},
                {'title': '用户消息', 'url': self.get_model_url(UserMessage, 'changelist')},
            )},
            {'title': '订单管理', 'menus': (
                {'title': '积分充值', 'url': self.get_model_url(JifenPay, 'changelist')},
            )},
            {'title': '系统管理', 'menus': (
                {'title': '用户咨询', 'url': self.get_model_url(UserAsk, 'changelist')},
                {'title': '首页轮播', 'url': self.get_model_url(Banner, 'changelist')},
                {'title': '权限分组', 'url': self.get_model_url(Group, 'changelist')},
                {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
                {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
            )},
        )


class EmailVerifyCodeAdmin(object):
    # 这些变量名都是固定的
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    readonly_fields = ['send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields =['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    readonly_fields = ['add_time']


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(EmailVerifyCode, EmailVerifyCodeAdmin)