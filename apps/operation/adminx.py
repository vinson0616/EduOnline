import xadmin

from .models import UserAsk, UserCourse, UserMessage, CourseComments, UserFavorite, JifenDetail


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']
    readonly_fields = ['add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']
    readonly_fields = ['add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'add_time']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    readonly_fields = ['add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comment', 'add_time']
    search_fields =['user', 'course', 'comment']
    list_filter = ['user', 'course', 'comment', 'add_time']
    readonly_fields = ['add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']
    readonly_fields = ['add_time']


class JifenDetailAdmin(object):
    list_display = ['user', 'type', 'nums', 'desc','add_time']
    search_fileds = ['user', 'type', 'nums', 'desc','add_time']
    list_filter = ['user', 'type', 'nums','desc', 'add_time']
    readonly_fields = ['add_time']
    ordering =['-add_time']


xadmin.site.register(JifenDetail, JifenDetailAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserAsk, UserAskAdmin)