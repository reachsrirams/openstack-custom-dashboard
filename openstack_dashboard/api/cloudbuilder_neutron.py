from openstack_dashboard import api

def get_network_name_mapping(request, tenant_id, **params):
    networks = api.neutron.network_list_for_tenant(request, tenant_id, **params)
    return create_network_name_mapping(networks)

def get_network_name_mapping(request, **params):
    networks = api.neutron.network_list(request, **params)
    return create_network_name_mapping(networks)

def create_network_name_mapping(networks):
    network_name_map = {}
    for n in networks:
        network_name_map[n.id] = n.name
    return network_name_map
