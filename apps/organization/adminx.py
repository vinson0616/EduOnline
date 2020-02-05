import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    #model_icon = 'fa fa-map'
    ordering = ['name']
    exclude = ['add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'category', 'tag','city', 'students', 'course_nums', 'click_num', 'fav_num']
    search_fields = ['name', 'desc','click_num', 'fav_num']
    list_filter = ['name', 'desc','click_num', 'fav_num', 'add_time']
    ordering = ['-click_num']
    readonly_fields = ['course_nums', 'click_num', 'fav_num','add_time']


class TeacherAdmin(object):
    list_display = ['name', 'Age', 'org', 'work_years', 'work_company', 'work_position','click_nums','fav_nums']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org', 'name', 'work_years', 'work_company']
    readonly_fields = ['click_nums', 'fav_nums', 'add_time']


xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CityDict, CityDictAdmin)