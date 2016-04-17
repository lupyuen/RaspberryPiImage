# -*- coding: utf-8 -*-

###############################################################################
#
# GetRecentMediaForUser
# Retrieves the most recent media published by a user.
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

class GetRecentMediaForUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRecentMediaForUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetRecentMediaForUser, self).__init__(temboo_session, '/Library/Instagram/GetRecentMediaForUser')


    def new_input_set(self):
        return GetRecentMediaForUserInputSet()

    def _make_result_set(self, result, path):
        return GetRecentMediaForUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecentMediaForUserChoreographyExecution(session, exec_id, path)

class GetRecentMediaForUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRecentMediaForUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth 2.0 process.)
        """
        super(GetRecentMediaForUserInputSet, self)._set_input('AccessToken', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The number of results to return.)
        """
        super(GetRecentMediaForUserInputSet, self)._set_input('Count', value)
    def set_MaxID(self, value):
        """
        Set the value of the MaxID input for this Choreo. ((optional, string) Return media liked before this id.)
        """
        super(GetRecentMediaForUserInputSet, self)._set_input('MaxID', value)
    def set_MinID(self, value):
        """
        Set the value of the MinID input for this Choreo. ((optional, string) Returns media later than this min_id.)
        """
        super(GetRecentMediaForUserInputSet, self)._set_input('MinID', value)
    def set_MinTimestamp(self, value):
        """
        Set the value of the MinTimestamp input for this Choreo. ((optional, date) Returns media after this UNIX timestamp.)
        """
        super(GetRecentMediaForUserInputSet, self)._set_input('MinTimestamp', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The ID of the user whose media to return. Defaults to 'self' indicating that the authenticating user is assumed.)
        """
        super(GetRecentMediaForUserInputSet, self)._set_input('UserID', value)

class GetRecentMediaForUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRecentMediaForUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class GetRecentMediaForUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetRecentMediaForUserResultSet(response, path)
