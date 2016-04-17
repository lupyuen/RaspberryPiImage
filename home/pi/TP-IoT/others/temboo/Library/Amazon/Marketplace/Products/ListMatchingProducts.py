# -*- coding: utf-8 -*-

###############################################################################
#
# ListMatchingProducts
# Returns a list of products and their attributes, ordered by relevancy, based on a search query that you specify.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListMatchingProducts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListMatchingProducts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListMatchingProducts, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Products/ListMatchingProducts')


    def new_input_set(self):
        return ListMatchingProductsInputSet()

    def _make_result_set(self, result, path):
        return ListMatchingProductsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListMatchingProductsChoreographyExecution(session, exec_id, path)

class ListMatchingProductsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListMatchingProducts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(ListMatchingProductsInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(ListMatchingProductsInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(ListMatchingProductsInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(ListMatchingProductsInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(ListMatchingProductsInputSet, self)._set_input('Endpoint', value)
    def set_MWSAuthToken(self, value):
        """
        Set the value of the MWSAuthToken input for this Choreo. ((optional, string) The Amazon MWS authorization token for the given seller and developer.)
        """
        super(ListMatchingProductsInputSet, self)._set_input('MWSAuthToken', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) A search string used to search for products.)
        """
        super(ListMatchingProductsInputSet, self)._set_input('Query', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(ListMatchingProductsInputSet, self)._set_input('ResponseFormat', value)

class ListMatchingProductsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListMatchingProducts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class ListMatchingProductsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListMatchingProductsResultSet(response, path)
