#
# Copyright (c) 2016 Wind River Systems, Inc.
#
# The right to copy, distribute, modify, or otherwise make use
# of this software may be licensed only pursuant to the terms
# of an applicable Wind River license agreement.
#

from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.api import base
from openstack_dashboard.dashboards.admin import dashboard


class SoftwareManagement(horizon.Panel):
    name = _("Software Management")
    slug = 'software_management'
    permissions = ('openstack.services.platform',)

    def allowed(self, context):
        if not base.is_service_enabled(context['request'], 'platform'):
            return False
        else:
            return super(SoftwareManagement, self).allowed(context)

    def nav(self, context):
        if not base.is_service_enabled(context['request'], 'platform'):
            return False
        else:
            return True


dashboard.Admin.register(SoftwareManagement)