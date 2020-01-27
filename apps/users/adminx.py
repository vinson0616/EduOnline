import xadmin
from xadmin import views

from .models import EmailVerifyCode, Banner


class BaseSetting(object):
    enable_themes = True  #主题开启
    use_bootswatch = True  #主题开启


class GlobalSettings(object):
    site_title = "百世利在线教育管理系统"  #页面左上角
    site_footer = "2020 百世利教育"
   # menu_style = "accordion"


class EmailVerifyCodeAdmin(object):
    # 这些变量名都是固定的
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields =['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyCode, EmailVerifyCodeAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)