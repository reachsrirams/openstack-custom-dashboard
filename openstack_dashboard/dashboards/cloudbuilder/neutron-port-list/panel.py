from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.cloudbuilder import dashboard

class Allports(horizon.Panel):
    name = _("All Ports")
    slug = "allports"


dashboard.Innervoice.register(Allports)
