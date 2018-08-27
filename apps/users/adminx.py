# __author__ = 'wilsonLwx'
# __date__ = '2018-8-27'

import xadmin
from xadmin import views
from .models import VerifyCode


# 主题
class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "xxx生鲜后台"
    site_footer = "xxx_shop"
    # menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_display = ["code", "mobile", "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
