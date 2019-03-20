import xadmin
from users.models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    # 显示字段
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索字段
    search_fields = ['code', 'email']
    # 过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
