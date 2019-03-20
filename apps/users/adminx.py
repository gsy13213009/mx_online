import xadmin
from users.models import EmailVerifyRecord, Banner
from xadmin import views


class BaseSetting(object):
    # 设置主题为可编辑
    enable_themes = True
    # 设置可选择的主题样式
    use_bootswatch = True

class GlobalSettings(object):
    # 修改后台的title
    site_title = '慕学后台系统'
    site_footer = '慕学在线网'
    # 修改后台的菜单栏可收起
    menu_style = 'accordion'

class EmailVerifyRecordAdmin(object):
    # 显示字段
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索字段
    search_fields = ['code', 'email']
    # 过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', ]
    search_fields = ['title', 'image', 'url', 'index', ]
    list_filter = ['title', 'image', 'url', 'index', ]


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
