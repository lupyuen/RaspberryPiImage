# -*- coding: utf-8 -*-

###############################################################################
#
# GetGist
# Returns an individual gist with a given id.
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

class GetGist(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetGist Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetGist, self).__init__(temboo_session, '/Library/GitHub/GistsAPI/Gists/GetGist')


    def new_input_set(self):
        return GetGistInputSet()

    def _make_result_set(self, result, path):
        return GetGistResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetGistChoreographyExecution(session, exec_id, path)

class GetGistInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetGist
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The Access Token retrieved during the OAuth process. Required when accessing a protected resource.)
        """
        super(GetGistInputSet, self)._set_input('AccessToken', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) The id for the gist you want to retrieve.)
        """
        super(GetGistInputSet, self)._set_input('ID', value)

class GetGistResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetGist Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from GitHub.)
        """
        return self._output.get('Response', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        return self._output.get('Remaining', None)

class GetGistChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetGistResultSet(response, path)
