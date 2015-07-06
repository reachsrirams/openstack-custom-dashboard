from django.utils.translation import ugettext_lazy as _

import horizon

class CloudBuilderDashboard(horizon.Dashboard):
    name = _("CloudBuilder")
    slug = "cloudbuilder"
    panels = ('neutron-port-list','neutron-subnet-list')
    default_panel = 'neutron-port-list'

horizon.register(CloudBuilderDashboard)
