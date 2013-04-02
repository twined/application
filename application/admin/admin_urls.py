# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Urls definition for the Application app
# (c) Twined/Univers 2009-2013. All rights reserved.
# ----------------------------------------------------------------------

from django.conf.urls import patterns, url, include
from django.conf import settings
from application.admin.views import DashboardIndex

urlpatterns = patterns(
    'admin',
    url(r'^$', DashboardIndex.as_view(), {}, name="dashboard"),
)

urlpatterns += patterns(
    '',
    url(r'^login/', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/', 'django.contrib.auth.views.logout', name="logout"),
)

# grab urls and configs from INSTALLED_APPS
for app in settings.INSTALLED_APPS:
    admin_cfg_dotpath = '%s.admin.config' % app
    admin_urls_dotpath = '%s.admin.urls' % app
    try:
        module = __import__(admin_cfg_dotpath, fromlist=[None])
        urlcfg = getattr(module, 'APP_ADMIN_URLS')
        urlpatterns += patterns(
            'admin',
            url(
                r'^%s/' % urlcfg['url_base'],
                include(
                    admin_urls_dotpath,
                    namespace=urlcfg['namespace'],
                )
            )
        )
    except ImportError:
        pass
    except AttributeError:
        pass
