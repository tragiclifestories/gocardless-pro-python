# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class PayoutsService(base_service.BaseService):
    """Service class that provides access to the payouts
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.Payout
    RESOURCE_NAME = 'payouts'


    def list(self,params=None, headers=None):
        """List payouts.

        Returns a [cursor-paginated](#api-usage-cursor-pagination) list of your
        payouts.

        Args:
              params (dict, optional): Query string parameters.

        Returns:
              Payout
        """
        path = '/payouts'
        
        response = self._perform_request('GET', path, params, headers,
                                         max_network_retries=3,
                                         retry_delay_in_seconds=0.5)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)
    
  

    def get(self,identity,params=None, headers=None):
        """Get a single payout.

        Retrieves the details of a single payout. For an example of how to
        reconcile the transactions in a payout, see [this
        guide](#events-reconciling-payouts-with-events).

        Args:
              identity (string): Unique identifier, beginning with "PO".
              params (dict, optional): Query string parameters.

        Returns:
              ListResponse of Payout instances
        """
        path = self._sub_url_params('/payouts/:identity', {
          
            'identity': identity,
          })
        
        response = self._perform_request('GET', path, params, headers,
                                         max_network_retries=3,
                                         retry_delay_in_seconds=0.5)
        return self._resource_for(response)
  
