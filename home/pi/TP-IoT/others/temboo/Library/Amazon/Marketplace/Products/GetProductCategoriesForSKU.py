# -*- coding: utf-8 -*-

###############################################################################
#
# GetProductCategoriesForSKU
# Returns the product categories that a product belongs to, including parent categories back to the root for the marketplace. This method uses a MarketplaceId and a SellerSKU to uniquely identify a product.
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

class GetProductCategoriesForSKU(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetProductCategoriesForSKU Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetProductCategoriesForSKU, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Products/GetProductCategoriesForSKU')


    def new_input_set(self):
        return GetProductCategoriesForSKUInputSet()

    def _make_result_set(self, result, path):
        return GetProductCategoriesForSKUResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetProductCategoriesForSKUChoreographyExecution(session, exec_id, path)

class GetProductCategoriesForSKUInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetProductCategoriesForSKU
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetProductCategoriesForSKUInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(GetProductCategoriesForSKUInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(GetProductCategoriesForSKUInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetProductCategoriesForSKUInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(GetProductCategoriesForSKUInputSet, self)._set_input('Endpoint', value)
    def set_MWSAuthToken(self, value):
        """
        Set the value of the MWSAuthToken input for this Choreo. ((optional, string) The Amazon MWS authorization token for the given seller and developer.)
        """
        super(GetProductCategoriesForSKUInputSet, self)._set_input('MWSAuthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(GetProductCategoriesForSKUInputSet, self)._set_input('ResponseFormat', value)
    def set_SellerSKU(self, value):
        """
        Set the value of the SellerSKU input for this Choreo. ((required, string) A SellerSKU value used to identify a product in the given marketplace.)
        """
        super(GetProductCategoriesForSKUInputSet, self)._set_input('SellerSKU', value)

class GetProductCategoriesForSKUResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetProductCategoriesForSKU Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class GetProductCategoriesForSKUChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetProductCategoriesForSKUResultSet(response, path)
