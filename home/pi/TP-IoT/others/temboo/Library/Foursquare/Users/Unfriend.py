# -*- coding: utf-8 -*-

###############################################################################
#
# Unfriend
# Cancels any relationship between the acting user and the specified user.
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

class Unfriend(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Unfriend Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Unfriend, self).__init__(temboo_session, '/Library/Foursquare/Users/Unfriend')


    def new_input_set(self):
        return UnfriendInputSet()

    def _make_result_set(self, result, path):
        return UnfriendResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UnfriendChoreographyExecution(session, exec_id, path)

class UnfriendInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Unfriend
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API Oauth token string.)
        """
        super(UnfriendInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(UnfriendInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID of a user to unfriend.)
        """
        super(UnfriendInputSet, self)._set_input('UserID', value)


class UnfriendResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Unfriend Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class UnfriendChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UnfriendResultSet(response, path)
