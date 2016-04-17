# -*- coding: utf-8 -*-

###############################################################################
#
# GetNextMessage
# Retrieves the next email from a user's inbox.
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

class GetNextMessage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetNextMessage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetNextMessage, self).__init__(temboo_session, '/Library/Google/Gmailv2/Messages/GetNextMessage')


    def new_input_set(self):
        return GetNextMessageInputSet()

    def _make_result_set(self, result, path):
        return GetNextMessageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNextMessageChoreographyExecution(session, exec_id, path)

class GetNextMessageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetNextMessage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth2 process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new Access Token.)
        """
        super(GetNextMessageInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(GetNextMessageInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(GetNextMessageInputSet, self)._set_input('ClientSecret', value)
    def set_EncodeMessage(self, value):
        """
        Set the value of the EncodeMessage input for this Choreo. ((optional, boolean) When set to "true" (the default), the message Body will be Base64 encoded.)
        """
        super(GetNextMessageInputSet, self)._set_input('EncodeMessage', value)
    def set_LabelID(self, value):
        """
        Set the value of the LabelID input for this Choreo. ((conditional, string) Returns messages with a label matching this ID (e.g., INBOX, UNREAD, Label_1, etc.))
        """
        super(GetNextMessageInputSet, self)._set_input('LabelID', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new Access Token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(GetNextMessageInputSet, self)._set_input('RefreshToken', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The ID of the acting user. Defaults to "me" indicating the user associated with the Access Token or Refresh Token provided.)
        """
        super(GetNextMessageInputSet, self)._set_input('UserID', value)

class GetNextMessageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetNextMessage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_Body(self):
        """
        Retrieve the value for the "Body" output from this Choreo execution. ((string) The message body.)
        """
        return self._output.get('Body', None)
    def get_From(self):
        """
        Retrieve the value for the "From" output from this Choreo execution. ((string) The sender address.)
        """
        return self._output.get('From', None)
    def get_MessageID(self):
        """
        Retrieve the value for the "MessageID" output from this Choreo execution. ((string) The ID of the message.)
        """
        return self._output.get('MessageID', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response code returned from Google. A 200 is expected for a successful request. A 404 indicates that the stored history id has become invalid or expired. See Choreo notes for more details.)
        """
        return self._output.get('ResponseStatusCode', None)
    def get_Snippet(self):
        """
        Retrieve the value for the "Snippet" output from this Choreo execution. ((string) The email body snippet.)
        """
        return self._output.get('Snippet', None)
    def get_Subject(self):
        """
        Retrieve the value for the "Subject" output from this Choreo execution. ((string) The message subject.)
        """
        return self._output.get('Subject', None)

class GetNextMessageChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetNextMessageResultSet(response, path)
