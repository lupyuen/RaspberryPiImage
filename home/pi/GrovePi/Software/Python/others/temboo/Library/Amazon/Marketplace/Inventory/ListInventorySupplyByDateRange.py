# -*- coding: utf-8 -*-

###############################################################################
#
# ListInventorySupplyByDateRange
# Returns information about the availability of a seller's inventory using a given date range.
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

class ListInventorySupplyByDateRange(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListInventorySupplyByDateRange Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListInventorySupplyByDateRange, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Inventory/ListInventorySupplyByDateRange')


    def new_input_set(self):
        return ListInventorySupplyByDateRangeInputSet()

    def _make_result_set(self, result, path):
        return ListInventorySupplyByDateRangeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListInventorySupplyByDateRangeChoreographyExecution(session, exec_id, path)

class ListInventorySupplyByDateRangeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListInventorySupplyByDateRange
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(ListInventorySupplyByDateRangeInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(ListInventorySupplyByDateRangeInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(ListInventorySupplyByDateRangeInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(ListInventorySupplyByDateRangeInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(ListInventorySupplyByDateRangeInputSet, self)._set_input('Endpoint', value)
    def set_MWSAuthToken(self, value):
        """
        Set the value of the MWSAuthToken input for this Choreo. ((optional, string) The Amazon MWS authorization token for the given seller and developer.)
        """
        super(ListInventorySupplyByDateRangeInputSet, self)._set_input('MWSAuthToken', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((conditional, string) The value returned in the NextPageToken output of this Choreo when there are multiple pages of inventory items to retrieve. Required unless providing QueryStartDateTime.)
        """
        super(ListInventorySupplyByDateRangeInputSet, self)._set_input('PageToken', value)
    def set_QueryStartDateTime(self, value):
        """
        Set the value of the QueryStartDateTime input for this Choreo. ((conditional, date) A date used for selecting items that have had changes in inventory availability after (or at) a specified time, in ISO 8601 date format (i.e. 2012-01-01). Required unless providing PageToken.)
        """
        super(ListInventorySupplyByDateRangeInputSet, self)._set_input('QueryStartDateTime', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(ListInventorySupplyByDateRangeInputSet, self)._set_input('ResponseFormat', value)
    def set_ResponseGroup(self, value):
        """
        Set the value of the ResponseGroup input for this Choreo. ((optional, string) Indicates whether or not to return the SupplyDetail element in the response. Valid values are: "Basic" (does not include SupplyDetail), and "Detailed" (includes SupplyDetail). Defaults to "Basic".)
        """
        super(ListInventorySupplyByDateRangeInputSet, self)._set_input('ResponseGroup', value)

class ListInventorySupplyByDateRangeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListInventorySupplyByDateRange Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)
    def get_NextPageToken(self):
        """
        Retrieve the value for the "NextPageToken" output from this Choreo execution. ((string) A token used to retrieve the next page of results. If a token is not returned, there are no more results to retrieve. This token can be passed to the PageToken input of this Choreo.)
        """
        return self._output.get('NextPageToken', None)

class ListInventorySupplyByDateRangeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListInventorySupplyByDateRangeResultSet(response, path)
