# -*- coding: utf-8 -*-

###############################################################################
#
# RefreshToken
# Refreshes an expired access token.
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

class RefreshToken(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RefreshToken Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RefreshToken, self).__init__(temboo_session, '/Library/Utilities/Authentication/OAuth2/RefreshToken')


    def new_input_set(self):
        return RefreshTokenInputSet()

    def _make_result_set(self, result, path):
        return RefreshTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RefreshTokenChoreographyExecution(session, exec_id, path)

class RefreshTokenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RefreshToken
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenEndpoint(self, value):
        """
        Set the value of the AccessTokenEndpoint input for this Choreo. ((required, string) The URL for the authorization server that issues access tokens (e.g. https://accounts.google.com/o/oauth2/token).)
        """
        super(RefreshTokenInputSet, self)._set_input('AccessTokenEndpoint', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((required, string) The Client ID provided by the service.)
        """
        super(RefreshTokenInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((required, string) The Client Secret provided by the service.)
        """
        super(RefreshTokenInputSet, self)._set_input('ClientSecret', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((required, string) The refresh token retrieved in the OAuth process to be used when your access token expires.)
        """
        super(RefreshTokenInputSet, self)._set_input('RefreshToken', value)

class RefreshTokenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RefreshToken Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the server.)
        """
        return self._output.get('Response', None)

class RefreshTokenChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RefreshTokenResultSet(response, path)
