from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    course_name = models.CharField(max_length=50, verbose_name="课程名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, verbose_name="评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name


class JifenDetail(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    type = models.CharField(max_length=50, verbose_name="积分类别", default='zj',
                            choices=(('zj', '注册'), ('jl', '奖励'), ('yq', '邀请'), ('cz', '充值'), ('xf', '消费'), ('tk', '退款')))
    nums = models.IntegerField(default=0, verbose_name="积分")
    desc = models.CharField(max_length=300, verbose_name="积分说明", default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "积分明细"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.desc


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0, verbose_name="数据id")
    fav_type = models.IntegerField(choices=((1,"课程"), (2, "课程机构"), (3,"讲师")), default=1, verbose_name="收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name="接受用户")
    message = models.CharField(max_length=500, verbose_name="消息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="购买用户", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="已购买课程", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="购买时间")

    class Meta:
        verbose_name = "购买课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name


