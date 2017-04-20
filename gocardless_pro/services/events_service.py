# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class EventsService(base_service.BaseService):
    """Service class that provides access to the events
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.Event
    RESOURCE_NAME = 'events'


    def list(self,params=None, headers=None):
        """List events.

        Returns a [cursor-paginated](#api-usage-cursor-pagination) list of your
        events.

        Args:
              params (dict, optional): Query string parameters.

        Returns:
              Event
        """
        path = '/events'
        
        response = self._perform_request('GET', path, params, headers,
                                         max_network_retries=3,
                                         retry_delay_in_seconds=0.5)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)
    
  

    def get(self,identity,params=None, headers=None):
        """Get a single event.

        Retrieves the details of a single event.

        Args:
              identity (string): Unique identifier, beginning with "EV".
              params (dict, optional): Query string parameters.

        Returns:
              ListResponse of Event instances
        """
        path = self._sub_url_params('/events/:identity', {
          
            'identity': identity,
          })
        
        response = self._perform_request('GET', path, params, headers,
                                         max_network_retries=3,
                                         retry_delay_in_seconds=0.5)
        return self._resource_for(response)
  
