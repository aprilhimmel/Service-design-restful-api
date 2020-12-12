from model.repository.endpoints_repo import EndpointRepo
er = EndpointRepo()


def get_all_endpoints(apiname):
    endpoints = er.get_all_endpoints(apiname)
    endpoints = [endpoint.to_dict() for endpoint in endpoints]
    return endpoints


def get_endpoint_uri(id):
    endpoint = er.get_endpoint_uri(id)
    return endpoint


def add_endpoint(apiid, data):
    er.add_endpoint(apiid, data)
    return

