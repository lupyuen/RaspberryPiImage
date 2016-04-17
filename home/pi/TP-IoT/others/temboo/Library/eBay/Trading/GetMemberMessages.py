# -*- coding: utf-8 -*-

###############################################################################
#
# GetMemberMessages
# Retrieves a list of the messages that buyers have posted about your active item listings.
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

class GetMemberMessages(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetMemberMessages Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetMemberMessages, self).__init__(temboo_session, '/Library/eBay/Trading/GetMemberMessages')


    def new_input_set(self):
        return GetMemberMessagesInputSet()

    def _make_result_set(self, result, path):
        return GetMemberMessagesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMemberMessagesChoreographyExecution(session, exec_id, path)

class GetMemberMessagesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetMemberMessages
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DisplayToPublic(self, value):
        """
        Set the value of the DisplayToPublic input for this Choreo. ((optional, boolean) When set to true, only public messages (viewable in the Item listing) are returned.)
        """
        super(GetMemberMessagesInputSet, self)._set_input('DisplayToPublic', value)
    def set_EndCreationTime(self, value):
        """
        Set the value of the EndCreationTime input for this Choreo. ((optional, date) Used to filter by date range (e.g., 2013-02-08T00:00:00.000Z).)
        """
        super(GetMemberMessagesInputSet, self)._set_input('EndCreationTime', value)
    def set_EntriesPerPage(self, value):
        """
        Set the value of the EntriesPerPage input for this Choreo. ((optional, integer) The maximum number of records to return in the result.)
        """
        super(GetMemberMessagesInputSet, self)._set_input('EntriesPerPage', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((optional, string) The ID of the item the message is about.)
        """
        super(GetMemberMessagesInputSet, self)._set_input('ItemID', value)
    def set_MailMessageType(self, value):
        """
        Set the value of the MailMessageType input for this Choreo. ((required, string) The type of message to retrieve. Valid values are: All and AskSellerQuestion. When set to AskSellerQuestion, ItemID or a date range filter must be specified.)
        """
        super(GetMemberMessagesInputSet, self)._set_input('MailMessageType', value)
    def set_MemberMessageID(self, value):
        """
        Set the value of the MemberMessageID input for this Choreo. ((optional, string) An ID that uniquely identifies the message for a given user to be retrieved.)
        """
        super(GetMemberMessagesInputSet, self)._set_input('MemberMessageID', value)
    def set_MessageStatus(self, value):
        """
        Set the value of the MessageStatus input for this Choreo. ((optional, string) The status of the message. Valid values are: Answered and Unanswered.)
        """
        super(GetMemberMessagesInputSet, self)._set_input('MessageStatus', value)
    def set_PageNumber(self, value):
        """
        Set the value of the PageNumber input for this Choreo. ((optional, integer) Specifies the page number of the results to return.)
        """
        super(GetMemberMessagesInputSet, self)._set_input('PageNumber', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetMemberMessagesInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(GetMemberMessagesInputSet, self)._set_input('SandboxMode', value)
    def set_SenderID(self, value):
        """
        Set the value of the SenderID input for this Choreo. ((optional, string) The seller's UserID.)
        """
        super(GetMemberMessagesInputSet, self)._set_input('SenderID', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(GetMemberMessagesInputSet, self)._set_input('SiteID', value)
    def set_StartCreationTime(self, value):
        """
        Set the value of the StartCreationTime input for this Choreo. ((optional, date) Used to filter by date range (e.g., 2013-02-08T00:00:00.000Z).)
        """
        super(GetMemberMessagesInputSet, self)._set_input('StartCreationTime', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        super(GetMemberMessagesInputSet, self)._set_input('UserToken', value)

class GetMemberMessagesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetMemberMessages Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class GetMemberMessagesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetMemberMessagesResultSet(response, path)
