# -*- coding: utf-8 -*-

###############################################################################
#
# LeaveFeedback
# Enables a buyer and seller to leave feedback for their order partner at the conclusion of a successful order.
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

class LeaveFeedback(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LeaveFeedback Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(LeaveFeedback, self).__init__(temboo_session, '/Library/eBay/Trading/LeaveFeedback')


    def new_input_set(self):
        return LeaveFeedbackInputSet()

    def _make_result_set(self, result, path):
        return LeaveFeedbackResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LeaveFeedbackChoreographyExecution(session, exec_id, path)

class LeaveFeedbackInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LeaveFeedback
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_LeaveFeedbackRequest(self, value):
        """
        Set the value of the LeaveFeedbackRequest input for this Choreo. ((optional, xml) The complete XML request body containing properties you wish to set. This can be used as an alternative to individual inputs that represent request properties.)
        """
        super(LeaveFeedbackInputSet, self)._set_input('LeaveFeedbackRequest', value)
    def set_CommentText(self, value):
        """
        Set the value of the CommentText input for this Choreo. ((conditional, string) The comment text to leave Feedback about the buyer.)
        """
        super(LeaveFeedbackInputSet, self)._set_input('CommentText', value)
    def set_CommentType(self, value):
        """
        Set the value of the CommentType input for this Choreo. ((conditional, string) The type of comment. Valid values are: Positive, Negative, and Neutral.)
        """
        super(LeaveFeedbackInputSet, self)._set_input('CommentType', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((conditional, string) The unique identifier for an eBay item listing that was sold. Required unless OrderLineItemID is specified.)
        """
        super(LeaveFeedbackInputSet, self)._set_input('ItemID', value)
    def set_OrderLineItemID(self, value):
        """
        Set the value of the OrderLineItemID input for this Choreo. ((optional, string) This is a unique identifier for an eBay order line item and is based upon the concatenation of ItemID and TransactionID, with a hyphen in between these two IDs.)
        """
        super(LeaveFeedbackInputSet, self)._set_input('OrderLineItemID', value)
    def set_RatingDetail(self, value):
        """
        Set the value of the RatingDetail input for this Choreo. ((conditional, string) The subject that is being rated. Valid values are: Communication, ItemAsDescribed, ShippingAndHandlingCharges, and ShippingTime.)
        """
        super(LeaveFeedbackInputSet, self)._set_input('RatingDetail', value)
    def set_Rating(self, value):
        """
        Set the value of the Rating input for this Choreo. ((conditional, integer) A detailed numeric rating (1 through 5) for an order line item. This rating is applied to the subject provided for RatingDetail.)
        """
        super(LeaveFeedbackInputSet, self)._set_input('Rating', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(LeaveFeedbackInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(LeaveFeedbackInputSet, self)._set_input('SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(LeaveFeedbackInputSet, self)._set_input('SiteID', value)
    def set_TargetUser(self, value):
        """
        Set the value of the TargetUser input for this Choreo. ((conditional, string) The user ID of the buyer who you want to leave feedback for.)
        """
        super(LeaveFeedbackInputSet, self)._set_input('TargetUser', value)
    def set_TransactionID(self, value):
        """
        Set the value of the TransactionID input for this Choreo. ((optional, string) The unique identifier for an eBay order line item (transaction). Required when there are multiple order ine items between the two order partners that require feedback.)
        """
        super(LeaveFeedbackInputSet, self)._set_input('TransactionID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        super(LeaveFeedbackInputSet, self)._set_input('UserToken', value)

class LeaveFeedbackResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LeaveFeedback Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class LeaveFeedbackChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return LeaveFeedbackResultSet(response, path)
