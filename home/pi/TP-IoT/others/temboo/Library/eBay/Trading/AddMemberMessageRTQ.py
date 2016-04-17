# -*- coding: utf-8 -*-

###############################################################################
#
# AddMemberMessageRTQ
# Allows a seller to reply to a question about an active item listing.
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

class AddMemberMessageRTQ(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddMemberMessageRTQ Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddMemberMessageRTQ, self).__init__(temboo_session, '/Library/eBay/Trading/AddMemberMessageRTQ')


    def new_input_set(self):
        return AddMemberMessageRTQInputSet()

    def _make_result_set(self, result, path):
        return AddMemberMessageRTQResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddMemberMessageRTQChoreographyExecution(session, exec_id, path)

class AddMemberMessageRTQInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddMemberMessageRTQ
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Body(self, value):
        """
        Set the value of the Body input for this Choreo. ((required, string) The message body which should answer the question that an eBay user ask the seller. HTML is not allowed.)
        """
        super(AddMemberMessageRTQInputSet, self)._set_input('Body', value)
    def set_DisplayToPublic(self, value):
        """
        Set the value of the DisplayToPublic input for this Choreo. ((optional, string) When set to true, this indicates that the member message is viewable in the item listing.)
        """
        super(AddMemberMessageRTQInputSet, self)._set_input('DisplayToPublic', value)
    def set_EmailCopyToSender(self, value):
        """
        Set the value of the EmailCopyToSender input for this Choreo. ((optional, boolean) A flag used to indicate that a copy should be sent to the sender.)
        """
        super(AddMemberMessageRTQInputSet, self)._set_input('EmailCopyToSender', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((optional, string) The unique ID of the item about which the question was asked.)
        """
        super(AddMemberMessageRTQInputSet, self)._set_input('ItemID', value)
    def set_ParentMessageID(self, value):
        """
        Set the value of the ParentMessageID input for this Choreo. ((required, string) The ID number of the question to which this message is responding.)
        """
        super(AddMemberMessageRTQInputSet, self)._set_input('ParentMessageID', value)
    def set_RecipientID(self, value):
        """
        Set the value of the RecipientID input for this Choreo. ((required, string) The recipient's eBay user ID.)
        """
        super(AddMemberMessageRTQInputSet, self)._set_input('RecipientID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(AddMemberMessageRTQInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(AddMemberMessageRTQInputSet, self)._set_input('SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(AddMemberMessageRTQInputSet, self)._set_input('SiteID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        super(AddMemberMessageRTQInputSet, self)._set_input('UserToken', value)

class AddMemberMessageRTQResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddMemberMessageRTQ Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class AddMemberMessageRTQChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddMemberMessageRTQResultSet(response, path)
