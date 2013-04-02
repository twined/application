# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Context processors for the Application app
# Provides {{ admin }} dictionary in all templates.
# (c) Twined/Univers 2009-2013. All rights reserved.
# ----------------------------------------------------------------------

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


def admin(request):
    try:
        cfg = getattr(settings, 'ADMIN_CONFIG')
    except AttributeError:
        raise ImproperlyConfigured(
            "'ADMIN_CONFIG' must be set in settings.py."
        )
    return {'admin': cfg}
