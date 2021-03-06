# Copyright (C) 2010-2013 Claudio Guarnieri.
# Copyright (C) 2014-2016 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file "docs/LICENSE" for copying permission.

from cuckoo.web.controllers.machines.api import MachinesApi
from django.conf.urls import url

urlpatterns = [
    url(r"^api/list/$", MachinesApi.list),
    url(r"^api/view/(?P<name>\w+)/$", MachinesApi.view),
]
