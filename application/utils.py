# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Utility functions for the Application app
# (c) Twined/Univers 2009-2013. All rights reserved.
# ----------------------------------------------------------------------

import json
import types

from django.core.serializers import serialize
from django.utils.simplejson import dumps, loads, JSONEncoder
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.db import models
from django.utils.functional import curry


def json_response(response_data):
    return HttpResponse(json.dumps(response_data),
                        mimetype="application/json")


class DjangoJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            # `default` must return a python serializable
            # structure, the easiest way is to load the JSON
            # string produced by `serialize` and return it
            return loads(serialize('json', obj))
        return JSONEncoder.default(self, obj)


dumps = curry(dumps, cls=DjangoJSONEncoder)


def to_json(obj):
    if isinstance(obj, QuerySet):
        return dumps(obj)
        #return dumps(obj, cls=DjangoJSONEncoder)
    if isinstance(obj, models.Model):
        # do the same as above by making it a queryset first
        set_obj = [obj]
        set_str = dumps(loads(serialize('json', set_obj)))
        # eliminate brackets in the beginning and the end
        str_obj = set_str[1:len(set_str) - 2]
    return str_obj


def merge_settings(default_settings, user_settings):
    # store a copy of default_settings, but overwrite with
    # user_settings's values where applicable
    merged = dict(default_settings, **user_settings)
    default_settings_keys = default_settings.keys()

    # if the value of merged[key] was overwritten with
    # user_settings[key]'s value then we need to put back any
    # missing default_settings[key] values
    for key in default_settings_keys:
        # if this key is a dictionary, recurse
        if isinstance(default_settings[key],
                      types.DictType) and key in user_settings:
            merged[key] = merge_settings(
                default_settings[key],
                user_settings[key]
            )

    return merged
