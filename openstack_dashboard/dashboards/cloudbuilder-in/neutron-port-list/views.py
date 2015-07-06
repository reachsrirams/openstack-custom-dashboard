from django.utils.datastructures import SortedDict
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import tables
from openstack_dashboard import api

from openstack_dashboard.dashboards.innervoice.allports import tables as allportstable

class IndexView(tables.DataTableView):
    # A very simple class-based view...
    table_class = allportstable.AllPortsTable
    template_name = 'innervoice/allports/index.html'

    def get_data(self):
        # Add data to the context here...
        ports = api.neutron.port_list(self.request)
        networks = api.neutron.network_list(self.request)
        netmap = {}
        for n in networks:
            netmap[n.id] = n.name
        for p in ports:
            p.network_name = netmap[p.network_id]
        return ports
