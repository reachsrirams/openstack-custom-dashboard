from django.utils.translation import ugettext_lazy as _

import horizon
from openstack_dashboard.dashboards.cloudbuilder import dashboard

class NeutronPortListPanel(horizon.Panel):
    name = _("Neutron Port List")
    slug = "neutronportlist"


dashboard.cloudbuilder.register(NeutronPortListPanel)
