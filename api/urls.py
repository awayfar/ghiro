# Ghiro - Copyright (C) 2013-2016 Ghiro Developers.
# This file is part of Ghiro.
# See the file 'docs/LICENSE.txt' for license terms.

from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r"^cases/new$", "api.views.new_case"),
    url(r"^cases/show$", "api.views.show_case"),
    url(r"^images/new$", "api.views.new_image"),
    url(r"^images/report", "api.views.get_report"),
)
