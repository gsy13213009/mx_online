import xadmin
from operation.models import *


class UserAskAdmin(object):
    list_display = ['name',
                    'mobile',
                    'course_name',
                    'add_time']


class CourseCommentAdmin(object):
    list_display = ['user',
                    'course',
                    'comment',
                    'add_time']
    search_fields = list_display
    list_filter = list_display


class UserFavoriteAdmin(object):
    list_display = ['user',
                    'fav_id',
                    'fav_type',
                    'add_time']
    search_fields = list_display
    list_filter = list_display


class UserMessageAdmin(object):
    list_display = ['user',
                    'message',
                    'has_read',
                    'add_time']
    search_fields = list_display
    list_filter = list_display


class UserCourseAdmin(object):
    list_display = ['user',
                    'course',
                    'add_time']
    search_fields = list_display
    list_filter = list_display


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)