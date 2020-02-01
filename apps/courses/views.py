from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from courses.models import Course, CourseResource, Video
from operation.models import UserFavorite, UserCourse, CourseComments
from utils.mixin_utils import LoginRequiredMixin


class CourseListView(View):

    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")
        hot_courses = Course.objects.all().order_by("-click_nums")[:3]

        # 课程全局搜索
        search_keywards = request.GET.get('keywords',"")
        if search_keywards:
            all_courses = all_courses.filter(Q(name__icontains=search_keywards)|Q(desc__icontains=search_keywards)|Q(detail__icontains=search_keywards))
        # 课程排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_nums")

        # 对课程进行分页显示
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 6, request=request)
        courses = p.page(page)

        return render(request, 'course-list.html', {
            "all_courses": courses,
            "hot_courses": hot_courses,
            "sort": sort
        })


class CourseDetailView(View):

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        # 增加课程点击数
        course.click_nums += 1
        course.save()

        has_fav_course = False
        has_fav_org = False
        has_buy_course = False

        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True
            if UserCourse.objects.filter(user=request.user, course=course):
                has_buy_course = True

        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses = []
        return render(request, "course-detail.html",{
           "course" : course,
            "relate_courses": relate_courses,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org,
            "has_buy_course": has_buy_course
        })


# 课程章节信息
class CourseInfoView(LoginRequiredMixin,View):

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 取出所有课程id
        course_ids =[user_course.course.id for user_course in all_user_courses]
        # 获取学过该用户学过其他的所有课程
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]

        all_resources = CourseResource.objects.filter(course=course)
        return render(request, "course-video.html", {
            "course": course,
            "all_resources": all_resources,
            "relate_courses": relate_courses
        })


# 课程评论
class CommentsView(LoginRequiredMixin,View):

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 取出所有课程id
        course_ids = [user_course.course.id for user_course in all_user_courses]
        # 获取学过该用户学过其他的所有课程
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]

        all_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.filter(course=course)
        return render(request, "course-comment.html", {
            "course": course,
            "all_resources": all_resources,
            "all_comments": all_comments,
            "relate_courses": relate_courses
        })


# 用户添加课程评论
class AddCommentView(LoginRequiredMixin,View):

    def post(self, request):
        # 判断用户是否登录
        if not request.user.is_authenticated:
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        course_id = request.POST.get("course_id", 0)
        comments = request.POST.get("comments", "")
        if int(course_id) >0 and comments:
            course_comment = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comment.course = course
            course_comment.user = request.user
            course_comment.comment = comments
            course_comment.save()
            return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加失败"}', content_type='application/json')


# 视频播放
class VideoPlayView(View):

    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        course = video.lesson.course
        return render(request, "course-play.html", {
            "course": course,
            "video": video
        })