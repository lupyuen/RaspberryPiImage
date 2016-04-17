# -*- coding: utf-8 -*-

###############################################################################
#
# ListUnsubscribe
# Remove a subscriber from a MailChimp list.
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

class ListUnsubscribe(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListUnsubscribe Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListUnsubscribe, self).__init__(temboo_session, '/Library/MailChimp/ListUnsubscribe')


    def new_input_set(self):
        return ListUnsubscribeInputSet()

    def _make_result_set(self, result, path):
        return ListUnsubscribeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListUnsubscribeChoreographyExecution(session, exec_id, path)

class ListUnsubscribeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListUnsubscribe
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp.)
        """
        super(ListUnsubscribeInputSet, self)._set_input('APIKey', value)
    def set_DeleteMember(self, value):
        """
        Set the value of the DeleteMember input for this Choreo. ((optional, boolean) A flag used to completely delete the member from your list instead of just unsubscribing. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        super(ListUnsubscribeInputSet, self)._set_input('DeleteMember', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((required, string) The email address to unsubscribe.)
        """
        super(ListUnsubscribeInputSet, self)._set_input('EmailAddress', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The id of the list that contains the email address you want to unsubscribe.)
        """
        super(ListUnsubscribeInputSet, self)._set_input('ListId', value)
    def set_SendGoodbye(self, value):
        """
        Set the value of the SendGoodbye input for this Choreo. ((optional, boolean) A flag used to send the goodbye email to the email address. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        super(ListUnsubscribeInputSet, self)._set_input('SendGoodbye', value)
    def set_SendNotify(self, value):
        """
        Set the value of the SendNotify input for this Choreo. ((optional, boolean) A flag used to send the unsubscribe notification email to the address defined in the list email notification settings. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        super(ListUnsubscribeInputSet, self)._set_input('SendNotify', value)

class ListUnsubscribeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListUnsubscribe Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mailchimp. Returns the string "true" for success and an error description for failures.)
        """
        return self._output.get('Response', None)

class ListUnsubscribeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListUnsubscribeResultSet(response, path)
