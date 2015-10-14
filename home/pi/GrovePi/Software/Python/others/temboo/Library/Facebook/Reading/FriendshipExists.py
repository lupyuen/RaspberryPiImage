# -*- coding: utf-8 -*-

###############################################################################
#
# FriendshipExists
# Determines whether two people are friends on Facebook.
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

class FriendshipExists(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FriendshipExists Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FriendshipExists, self).__init__(temboo_session, '/Library/Facebook/Reading/FriendshipExists')


    def new_input_set(self):
        return FriendshipExistsInputSet()

    def _make_result_set(self, result, path):
        return FriendshipExistsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FriendshipExistsChoreographyExecution(session, exec_id, path)

class FriendshipExistsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FriendshipExists
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final OAuth step.)
        """
        super(FriendshipExistsInputSet, self)._set_input('AccessToken', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The ID of the user whose friends list you want to check the UserID against. Defaults to "me" indicating the authenticated user.)
        """
        super(FriendshipExistsInputSet, self)._set_input('ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(FriendshipExistsInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID of the user to check against the acting user's list of friends.)
        """
        super(FriendshipExistsInputSet, self)._set_input('UserID', value)

class FriendshipExistsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FriendshipExists Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def get_IsFriend(self):
        """
        Retrieve the value for the "IsFriend" output from this Choreo execution. ((boolean) Returns as true or false depending on whether or not the UserID specified corresponds to a friend of the acting user.)
        """
        return self._output.get('IsFriend', None)

class FriendshipExistsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FriendshipExistsResultSet(response, path)
