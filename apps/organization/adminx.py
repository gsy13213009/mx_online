import xadmin
from organization.models import *


class CityDictAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = list_display
    list_filter = list_display


class CourseOrgAdmin(object):
    list_display = ['name',
                    'desc',
                    'click_nums',
                    'fav_nums',
                    'address',
                    'image',
                    'city',
                    'add_time']
    search_fields = list_display
    list_filter = list_display


class TeacherAdmin(object):
    list_display = ['org',
                    'name',
                    'work_year',
                    'work_company',
                    'work_position',
                    'points',
                    'click_nums',
                    'fav_nums',
                    'add_time']
    search_fields = list_display
    list_filter = list_display


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
