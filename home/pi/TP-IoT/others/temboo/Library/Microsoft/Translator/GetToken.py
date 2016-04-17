# -*- coding: utf-8 -*-

###############################################################################
#
# GetToken
# Retrieves an access token that can be used to authenticate with the Microsoft Translator API.
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

class GetToken(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetToken Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetToken, self).__init__(temboo_session, '/Library/Microsoft/Translator/GetToken')


    def new_input_set(self):
        return GetTokenInputSet()

    def _make_result_set(self, result, path):
        return GetTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTokenChoreographyExecution(session, exec_id, path)

class GetTokenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetToken
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((required, string) The Client ID obtained when signing up for Microsoft Translator on Azure Marketplace.)
        """
        super(GetTokenInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((required, string) The Client Secret obtained when signing up for Microsoft Translator on Azure Marketplace.)
        """
        super(GetTokenInputSet, self)._set_input('ClientSecret', value)

class GetTokenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetToken Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_AccessToken(self):
        """
        Retrieve the value for the "AccessToken" output from this Choreo execution. ((string) The access token returned from Microsoft.)
        """
        return self._output.get('AccessToken', None)
    def get_ExpiresIn(self):
        """
        Retrieve the value for the "ExpiresIn" output from this Choreo execution. ((integer) The number of seconds for which the access token is valid.)
        """
        return self._output.get('ExpiresIn', None)

class GetTokenChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTokenResultSet(response, path)
