from django.utils.translation import ugettext_lazy as _

import horizon

class CloudBuilderDashboard(horizon.Dashboard):
    name = _("CloudBuilder")
    slug = "cloudbuilder"
    panels = ('neutronportlist','neutronsubnetlist')
    default_panel = 'neutronportlist'

horizon.register(CloudBuilderDashboard)
