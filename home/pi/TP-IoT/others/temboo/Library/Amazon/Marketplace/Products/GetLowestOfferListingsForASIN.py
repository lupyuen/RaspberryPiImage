# -*- coding: utf-8 -*-

###############################################################################
#
# GetLowestOfferListingsForASIN
# Returns the lowest price offer listings for specific products by item condition. This method uses a MarketplaceId and ASIN values to uniquely identify products.
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

class GetLowestOfferListingsForASIN(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLowestOfferListingsForASIN Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLowestOfferListingsForASIN, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Products/GetLowestOfferListingsForASIN')


    def new_input_set(self):
        return GetLowestOfferListingsForASINInputSet()

    def _make_result_set(self, result, path):
        return GetLowestOfferListingsForASINResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLowestOfferListingsForASINChoreographyExecution(session, exec_id, path)

class GetLowestOfferListingsForASINInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLowestOfferListingsForASIN
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ASIN(self, value):
        """
        Set the value of the ASIN input for this Choreo. ((required, string) A comma-separated list of up to 20 ASIN values used to identify products in the given marketplace.)
        """
        super(GetLowestOfferListingsForASINInputSet, self)._set_input('ASIN', value)
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetLowestOfferListingsForASINInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(GetLowestOfferListingsForASINInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(GetLowestOfferListingsForASINInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetLowestOfferListingsForASINInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(GetLowestOfferListingsForASINInputSet, self)._set_input('Endpoint', value)
    def set_ItemCondition(self, value):
        """
        Set the value of the ItemCondition input for this Choreo. ((optional, string) Filters the offer listings to be considered based on item condition. Valid values: New, Used, Collectible, Refurbished, Club.)
        """
        super(GetLowestOfferListingsForASINInputSet, self)._set_input('ItemCondition', value)
    def set_MWSAuthToken(self, value):
        """
        Set the value of the MWSAuthToken input for this Choreo. ((optional, string) The Amazon MWS authorization token for the given seller and developer.)
        """
        super(GetLowestOfferListingsForASINInputSet, self)._set_input('MWSAuthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(GetLowestOfferListingsForASINInputSet, self)._set_input('ResponseFormat', value)

class GetLowestOfferListingsForASINResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLowestOfferListingsForASIN Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class GetLowestOfferListingsForASINChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLowestOfferListingsForASINResultSet(response, path)
