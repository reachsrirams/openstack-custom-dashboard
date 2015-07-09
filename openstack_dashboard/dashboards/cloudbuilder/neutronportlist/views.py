from horizon import tables
from openstack_dashboard import api

import openstack_dashboard.dashboards.cloudbuilder.neutronportlist as neutronportlist

class IndexView(tables.DataTableView):
    # A very simple class-based view...
    table_class = neutronportlist.tables.NeutronPortListTable
    template_name = 'cloudbuilder/neutronportlist/index.html'

    def get_data(self):
        # Add data to the context here...
        ports = api.neutron.port_list(self.request)
        network_name_mapping = api.cloudbuilder_neutron.get_network_name_mapping(self.request)
        for p in ports:
            p.network_name = network_name_mapping[p.network_id]
        return ports
