from datetime import datetime

from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(max_length=2, choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')))
    learn_times = models.IntegerField(default=0, verbose_name='学习时长')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='course/%Y/%m', verbose_name='封面图')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='章节名')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '课程名字'
        verbose_name_plural = verbose_name


class Video(models.Model):
    course = models.ForeignKey(Course, verbose_name='章节', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='视频名')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '视频名字'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='视频名')
    add_time = models.DateTimeField(default=datetime.now)
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='资源文件')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
