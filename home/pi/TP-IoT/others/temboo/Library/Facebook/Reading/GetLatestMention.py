# -*- coding: utf-8 -*-

###############################################################################
#
# GetLatestMention
# Retrieves the latest status update in a user's feed that mentions the specified user.
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

class GetLatestMention(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLatestMention Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLatestMention, self).__init__(temboo_session, '/Library/Facebook/Reading/GetLatestMention')


    def new_input_set(self):
        return GetLatestMentionInputSet()

    def _make_result_set(self, result, path):
        return GetLatestMentionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLatestMentionChoreographyExecution(session, exec_id, path)

class GetLatestMentionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLatestMention
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(GetLatestMentionInputSet, self)._set_input('AccessToken', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the user who is mentioned.)
        """
        super(GetLatestMentionInputSet, self)._set_input('Name', value)
    def set_ResponseMode(self, value):
        """
        Set the value of the ResponseMode input for this Choreo. ((optional, string) Used to simplify the response. Valid values are: simple and verbose. When set to simple, only the message string is returned. Verbose mode returns additional metadata. Defaults to "simple".)
        """
        super(GetLatestMentionInputSet, self)._set_input('ResponseMode', value)

class GetLatestMentionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLatestMention Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook.)
        """
        return self._output.get('Response', None)

class GetLatestMentionChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLatestMentionResultSet(response, path)
