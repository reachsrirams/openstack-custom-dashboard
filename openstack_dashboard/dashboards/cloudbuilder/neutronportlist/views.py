from django.utils.datastructures import SortedDict
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import tables
from openstack_dashboard import api

from openstack_dashboard.dashboards.cloudbuilder.neutronportlist import tables as neutronportlisttable

class IndexView(tables.DataTableView):
    # A very simple class-based view...
    table_class = neutronportlisttable.NeutronPortListTable
    template_name = 'cloudbuilder/neutronportlist/index.html'

    def get_data(self):
        # Add data to the context here...
        ports = api.neutron.port_list(self.request)
        netmap = api.cloudbuilder_neutron.get_network_name_mapping(self.request)
        for p in ports:
            p.network_name = netmap[p.network_id]
        return ports
