from src import centres,providers


class search_for_a_healthcare_service():

    def __init__(self,by_centre_name,by_suburb,by_service_type,by_provider_name):
        self._centres = []
        self._providers = []
        self._by_centre_name = by_centre_name
        self._by_suburb = by_suburb
        self._by_service = by_service
        self._by_provider_name = by_provider_name
        
        
    def search_by_centre_name(self,centre_name):
        #result = []
        for centre in self._centres:
            if centre.get_name() == centre_name:
                service = get_service(centre_name)
                #result.append(service)
                #return result
                return service
                
                
    def search_by_provider_name(self,provider_name):
        for provider in self._providers:
            if provider.get_name() == provider_name:
                service = get_service(provider_name)
                return service
                
    def search_by_suburb(self,suburb):
        for suburb in self._centres:
            if suburb.get_suburb() == suburb:
                service = get_service()
                return service
                
    def search_by_service_type(self,service_type):
        for s_type in self._providers:
            if s_type.get_types() == servide_type:
                service = get_service()
                return service
                                       
