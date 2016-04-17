# -*- coding: utf-8 -*-

###############################################################################
#
# GetUnreadMessages
# Retrieves a list of messages in the authenticating user's inbox that are marked as unread.
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

class GetUnreadMessages(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUnreadMessages Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetUnreadMessages, self).__init__(temboo_session, '/Library/Facebook/Reading/GetUnreadMessages')


    def new_input_set(self):
        return GetUnreadMessagesInputSet()

    def _make_result_set(self, result, path):
        return GetUnreadMessagesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUnreadMessagesChoreographyExecution(session, exec_id, path)

class GetUnreadMessagesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUnreadMessages
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(GetUnreadMessagesInputSet, self)._set_input('AccessToken', value)
    def set_ResponseMode(self, value):
        """
        Set the value of the ResponseMode input for this Choreo. ((optional, string) Used to simplify the response. Valid values are: simple and verbose. When set to simple, only an array of messages are returned. Verbose mode returns additional metadata. Defaults to "simple".)
        """
        super(GetUnreadMessagesInputSet, self)._set_input('ResponseMode', value)

class GetUnreadMessagesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUnreadMessages Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Facebook.)
        """
        return self._output.get('Response', None)

class GetUnreadMessagesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetUnreadMessagesResultSet(response, path)
