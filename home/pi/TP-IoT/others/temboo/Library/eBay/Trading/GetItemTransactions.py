# -*- coding: utf-8 -*-

###############################################################################
#
# GetItemTransactions
# Retrieves order line item (transaction) information for a specified ItemID.
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

class GetItemTransactions(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetItemTransactions Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetItemTransactions, self).__init__(temboo_session, '/Library/eBay/Trading/GetItemTransactions')


    def new_input_set(self):
        return GetItemTransactionsInputSet()

    def _make_result_set(self, result, path):
        return GetItemTransactionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetItemTransactionsChoreographyExecution(session, exec_id, path)

class GetItemTransactionsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetItemTransactions
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DetailLevel(self, value):
        """
        Set the value of the DetailLevel input for this Choreo. ((optional, string) The detail level of the response. Valid values are: ItemReturnDescription and ReturnAll.)
        """
        super(GetItemTransactionsInputSet, self)._set_input('DetailLevel', value)
    def set_EntriesPerPage(self, value):
        """
        Set the value of the EntriesPerPage input for this Choreo. ((optional, integer) The maximum number of records to return in the result.)
        """
        super(GetItemTransactionsInputSet, self)._set_input('EntriesPerPage', value)
    def set_IncludeContainingOrder(self, value):
        """
        Set the value of the IncludeContainingOrder input for this Choreo. ((optional, boolean) When set to true, the ContainingOrder container is returned in the response for each transaction node.)
        """
        super(GetItemTransactionsInputSet, self)._set_input('IncludeContainingOrder', value)
    def set_IncludeFinalValueFee(self, value):
        """
        Set the value of the IncludeFinalValueFee input for this Choreo. ((optional, boolean) When set to true, the Final Value Fee (FVF) for all order line items is returned in the response.)
        """
        super(GetItemTransactionsInputSet, self)._set_input('IncludeFinalValueFee', value)
    def set_IncludeVariations(self, value):
        """
        Set the value of the IncludeVariations input for this Choreo. ((optional, boolean) When set to true, all variations defined for the item are returned at the root level.)
        """
        super(GetItemTransactionsInputSet, self)._set_input('IncludeVariations', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((required, string) The unique identifier for an eBay item listing.)
        """
        super(GetItemTransactionsInputSet, self)._set_input('ItemID', value)
    def set_ModTimeFrom(self, value):
        """
        Set the value of the ModTimeFrom input for this Choreo. ((optional, date) Used to filter by date range (e.g., 2013-02-08T00:00:00.000Z).)
        """
        super(GetItemTransactionsInputSet, self)._set_input('ModTimeFrom', value)
    def set_ModTimeTo(self, value):
        """
        Set the value of the ModTimeTo input for this Choreo. ((optional, date) Used to filter by date range (e.g., 2013-02-08T00:00:00.000Z).)
        """
        super(GetItemTransactionsInputSet, self)._set_input('ModTimeTo', value)
    def set_NumberOfDays(self, value):
        """
        Set the value of the NumberOfDays input for this Choreo. ((optional, integer) The number of days in the past to search for order line items.)
        """
        super(GetItemTransactionsInputSet, self)._set_input('NumberOfDays', value)
    def set_OrderLineItemID(self, value):
        """
        Set the value of the OrderLineItemID input for this Choreo. ((optional, string) A unique identifier for an eBay order line item.)
        """
        super(GetItemTransactionsInputSet, self)._set_input('OrderLineItemID', value)
    def set_PageNumber(self, value):
        """
        Set the value of the PageNumber input for this Choreo. ((optional, integer) Specifies the page number of the results to return.)
        """
        super(GetItemTransactionsInputSet, self)._set_input('PageNumber', value)
    def set_Platform(self, value):
        """
        Set the value of the Platform input for this Choreo. ((optional, string) The name of the eBay co-branded site upon which the order line item was created. Valid values are: eBay, Express, Half, Shopping, or WorldOfGood.)
        """
        super(GetItemTransactionsInputSet, self)._set_input('Platform', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetItemTransactionsInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(GetItemTransactionsInputSet, self)._set_input('SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(GetItemTransactionsInputSet, self)._set_input('SiteID', value)
    def set_TransactionID(self, value):
        """
        Set the value of the TransactionID input for this Choreo. ((optional, string) Include a TransactionID field in the request if you want to retrieve the data for a specific order line item (transaction).)
        """
        super(GetItemTransactionsInputSet, self)._set_input('TransactionID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        super(GetItemTransactionsInputSet, self)._set_input('UserToken', value)

class GetItemTransactionsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetItemTransactions Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class GetItemTransactionsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetItemTransactionsResultSet(response, path)
