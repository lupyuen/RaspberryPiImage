# -*- coding: utf-8 -*-

###############################################################################
#
# CompleteSale
# Allows the seller to perform the final steps for completing an order.
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

class CompleteSale(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CompleteSale Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CompleteSale, self).__init__(temboo_session, '/Library/eBay/Trading/CompleteSale')


    def new_input_set(self):
        return CompleteSaleInputSet()

    def _make_result_set(self, result, path):
        return CompleteSaleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompleteSaleChoreographyExecution(session, exec_id, path)

class CompleteSaleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CompleteSale
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CompleteSaleRequest(self, value):
        """
        Set the value of the CompleteSaleRequest input for this Choreo. ((optional, xml) The complete XML request body containing properties you wish to set. This can be used as an alternative to individual inputs that represent request properties.)
        """
        super(CompleteSaleInputSet, self)._set_input('CompleteSaleRequest', value)
    def set_CommentText(self, value):
        """
        Set the value of the CommentText input for this Choreo. ((optional, string) The comment text to leave Feedback about the buyer.)
        """
        super(CompleteSaleInputSet, self)._set_input('CommentText', value)
    def set_CommentType(self, value):
        """
        Set the value of the CommentType input for this Choreo. ((optional, string) The type of comment. Valid values are: Positive.)
        """
        super(CompleteSaleInputSet, self)._set_input('CommentType', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((conditional, string) The unique identifier for an eBay item listing that was sold. Either ItemID or TransactionID should be provided.)
        """
        super(CompleteSaleInputSet, self)._set_input('ItemID', value)
    def set_Notes(self, value):
        """
        Set the value of the Notes input for this Choreo. ((optional, string) A text field for shipping related notes.)
        """
        super(CompleteSaleInputSet, self)._set_input('Notes', value)
    def set_OrderID(self, value):
        """
        Set the value of the OrderID input for this Choreo. ((optional, string) A unique identifier that identifies a single line item or multiple line item order.)
        """
        super(CompleteSaleInputSet, self)._set_input('OrderID', value)
    def set_OrderLineItemID(self, value):
        """
        Set the value of the OrderLineItemID input for this Choreo. ((optional, string) This is a unique identifier for an eBay order line item and is based upon the concatenation of ItemID and TransactionID, with a hyphen in between these two IDs.)
        """
        super(CompleteSaleInputSet, self)._set_input('OrderLineItemID', value)
    def set_Paid(self, value):
        """
        Set the value of the Paid input for this Choreo. ((conditional, boolean) Set to true to indicate that the item has been paid for. One of Feedback info, Shipped status or Paid status is required.)
        """
        super(CompleteSaleInputSet, self)._set_input('Paid', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(CompleteSaleInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(CompleteSaleInputSet, self)._set_input('SandboxMode', value)
    def set_ShipmentTrackingNumber(self, value):
        """
        Set the value of the ShipmentTrackingNumber input for this Choreo. ((optional, string) The tracking number for the package.)
        """
        super(CompleteSaleInputSet, self)._set_input('ShipmentTrackingNumber', value)
    def set_ShippedTime(self, value):
        """
        Set the value of the ShippedTime input for this Choreo. ((optional, date) The date and time that the item was shipped.)
        """
        super(CompleteSaleInputSet, self)._set_input('ShippedTime', value)
    def set_Shipped(self, value):
        """
        Set the value of the Shipped input for this Choreo. ((conditional, boolean) Set to true to indicate that the item has been shipped. One of Feedback info, Shipped status or Paid status is required.)
        """
        super(CompleteSaleInputSet, self)._set_input('Shipped', value)
    def set_ShippingCarrierUsed(self, value):
        """
        Set the value of the ShippingCarrierUsed input for this Choreo. ((optional, string) The carrier used to ship the item.)
        """
        super(CompleteSaleInputSet, self)._set_input('ShippingCarrierUsed', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(CompleteSaleInputSet, self)._set_input('SiteID', value)
    def set_TargetUser(self, value):
        """
        Set the value of the TargetUser input for this Choreo. ((optional, string) The user ID of the buyer who you want to leave feedback for.)
        """
        super(CompleteSaleInputSet, self)._set_input('TargetUser', value)
    def set_TransactionID(self, value):
        """
        Set the value of the TransactionID input for this Choreo. ((conditional, string) The unique identifier for an eBay order line item (transaction). Either ItemID or TransactionID should be provided.)
        """
        super(CompleteSaleInputSet, self)._set_input('TransactionID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        super(CompleteSaleInputSet, self)._set_input('UserToken', value)

class CompleteSaleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CompleteSale Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class CompleteSaleChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CompleteSaleResultSet(response, path)
