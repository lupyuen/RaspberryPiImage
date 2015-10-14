# -*- coding: utf-8 -*-

###############################################################################
#
# ListOrdersWithBuyerEmail
# Returns orders associated with a buyer's email address that you specify.
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

class ListOrdersWithBuyerEmail(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListOrdersWithBuyerEmail Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListOrdersWithBuyerEmail, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Orders/ListOrdersWithBuyerEmail')


    def new_input_set(self):
        return ListOrdersWithBuyerEmailInputSet()

    def _make_result_set(self, result, path):
        return ListOrdersWithBuyerEmailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListOrdersWithBuyerEmailChoreographyExecution(session, exec_id, path)

class ListOrdersWithBuyerEmailInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListOrdersWithBuyerEmail
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(ListOrdersWithBuyerEmailInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(ListOrdersWithBuyerEmailInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(ListOrdersWithBuyerEmailInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(ListOrdersWithBuyerEmailInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_BuyerEmail(self, value):
        """
        Set the value of the BuyerEmail input for this Choreo. ((required, string) The e-mail address of a buyer. Used to select only the orders that contain the specified e-mail address.)
        """
        super(ListOrdersWithBuyerEmailInputSet, self)._set_input('BuyerEmail', value)
    def set_CreatedAfter(self, value):
        """
        Set the value of the CreatedAfter input for this Choreo. ((optional, date) A date used for selecting orders created after (or at) a specified time, in ISO 8601 date format (i.e. 2012-01-01). Defaults to today's date if not provided.)
        """
        super(ListOrdersWithBuyerEmailInputSet, self)._set_input('CreatedAfter', value)
    def set_CreatedBefore(self, value):
        """
        Set the value of the CreatedBefore input for this Choreo. ((optional, date) A date used for selecting orders created before (or at) a specified time, in ISO 8601 date format (i.e. 2012-01-01).)
        """
        super(ListOrdersWithBuyerEmailInputSet, self)._set_input('CreatedBefore', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(ListOrdersWithBuyerEmailInputSet, self)._set_input('Endpoint', value)
    def set_MWSAuthToken(self, value):
        """
        Set the value of the MWSAuthToken input for this Choreo. ((optional, string) The Amazon MWS authorization token for the given seller and developer.)
        """
        super(ListOrdersWithBuyerEmailInputSet, self)._set_input('MWSAuthToken', value)
    def set_MaxResultsPerPage(self, value):
        """
        Set the value of the MaxResultsPerPage input for this Choreo. ((optional, integer) A number that indicates the maximum number of orders that can be returned per page. Valid values are: 1-100.)
        """
        super(ListOrdersWithBuyerEmailInputSet, self)._set_input('MaxResultsPerPage', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(ListOrdersWithBuyerEmailInputSet, self)._set_input('ResponseFormat', value)

class ListOrdersWithBuyerEmailResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListOrdersWithBuyerEmail Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class ListOrdersWithBuyerEmailChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListOrdersWithBuyerEmailResultSet(response, path)
