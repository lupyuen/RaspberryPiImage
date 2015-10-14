# -*- coding: utf-8 -*-

###############################################################################
#
# GetLatestPrivateMessage
# Retrieves the latest private message in a user's inbox.
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

class GetLatestPrivateMessage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLatestPrivateMessage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLatestPrivateMessage, self).__init__(temboo_session, '/Library/Facebook/Reading/GetLatestPrivateMessage')


    def new_input_set(self):
        return GetLatestPrivateMessageInputSet()

    def _make_result_set(self, result, path):
        return GetLatestPrivateMessageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLatestPrivateMessageChoreographyExecution(session, exec_id, path)

class GetLatestPrivateMessageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLatestPrivateMessage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(GetLatestPrivateMessageInputSet, self)._set_input('AccessToken', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the profile to retrieve the latest message for. Defaults to "me" indicating the authenticated user.)
        """
        super(GetLatestPrivateMessageInputSet, self)._set_input('ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(GetLatestPrivateMessageInputSet, self)._set_input('ResponseFormat', value)

class GetLatestPrivateMessageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLatestPrivateMessage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def get_CreatedTime(self):
        """
        Retrieve the value for the "CreatedTime" output from this Choreo execution. ((date) The date that the latest message was created.)
        """
        return self._output.get('CreatedTime', None)
    def get_FromID(self):
        """
        Retrieve the value for the "FromID" output from this Choreo execution. ((string) The ID of the message sender.)
        """
        return self._output.get('FromID', None)
    def get_FromName(self):
        """
        Retrieve the value for the "FromName" output from this Choreo execution. ((string) The name of the message sender.)
        """
        return self._output.get('FromName', None)
    def get_ID(self):
        """
        Retrieve the value for the "ID" output from this Choreo execution. ((string) The ID of the message.)
        """
        return self._output.get('ID', None)
    def get_Message(self):
        """
        Retrieve the value for the "Message" output from this Choreo execution. ((string) The latest private message.)
        """
        return self._output.get('Message', None)

class GetLatestPrivateMessageChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLatestPrivateMessageResultSet(response, path)
