# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator

class CreditorsService(base_service.BaseService):
    """Service class that provides access to the creditors
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.Creditor
    RESOURCE_NAME = 'creditors'
    def create(self, params=None, headers=None):
        """Create a creditor.

        Creates a new creditor.

        Args:
          params (dict, optional): Request body.

        Returns:
          Creditor
        """
        path = '/creditors'
        
        if params is not None:
            params = {self._envelope_key(): params}
        response = self._perform_request('POST', path, params, headers,
                                         retries=3,
                                         retry_delay_seconds=0.5)
        return self._resource_for(response)
    def list(self, params=None, headers=None):
        """List creditors.

        Returns a [cursor-paginated](#api-usage-cursor-pagination) list of your
        creditors.

        Args:
          params (dict, optional): Query string parameters.

        Returns:
          ListResponse of Creditor instances
        """
        path = '/creditors'
        
        response = self._perform_request('GET', path, params, headers,
                                         retries=3,
                                         retry_delay_seconds=0.5)
        return self._resource_for(response)

    def all(self, params=None):
        if params is None:
            params = {}
        return Paginator(self, params)

    def get(self, identity, params=None, headers=None):
        """Get a single creditor.

        Retrieves the details of an existing creditor.

        Args:identity
           (string): Unique identifier, beginning with "CR".
          params (dict, optional): Query string parameters.

        Returns:
          Creditor
        """
        path = self._sub_url_params('/creditors/:identity', {
          
            'identity': identity,
          })
        
        response = self._perform_request('GET', path, params, headers,
                                         retries=3,
                                         retry_delay_seconds=0.5)
        return self._resource_for(response)
    def update(self, identity, params=None, headers=None):
        """Update a creditor.

        Updates a creditor object. Supports all of the fields supported when
        creating a creditor.

        Args:identity
           (string): Unique identifier, beginning with "CR".
          params (dict, optional): Request body.

        Returns:
          Creditor
        """
        path = self._sub_url_params('/creditors/:identity', {
          
            'identity': identity,
          })
        
        if params is not None:
            params = {self._envelope_key(): params}
        response = self._perform_request('PUT', path, params, headers,
                                         retries=3,
                                         retry_delay_seconds=0.5)
        return self._resource_for(response)
