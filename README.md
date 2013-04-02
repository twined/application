APPLICATION
===========

**NOTE: This is tailored for the twined project structure, it probably won't work too well without customization on other project bootstraps.**

Installation:
-------------

    pip install -e git://github.com/twined/application.git#egg=application-dev

Add `application` to `INSTALLED_APPS` in your `conf/settings.py`


Usage:
------

Remember to add an `ADMIN_CONFIG` dict to your `settings.py`

    ADMIN_CONFIG = {
        'site_name': 'Application display name',
        'site_url': 'www.urlgoeshere.com',
    }