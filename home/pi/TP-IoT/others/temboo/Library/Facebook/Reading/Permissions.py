# -*- coding: utf-8 -*-

###############################################################################
#
# Permissions
# Retrieves the set of permissions associated with a given access token.
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

class Permissions(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Permissions Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Permissions, self).__init__(temboo_session, '/Library/Facebook/Reading/Permissions')


    def new_input_set(self):
        return PermissionsInputSet()

    def _make_result_set(self, result, path):
        return PermissionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PermissionsChoreographyExecution(session, exec_id, path)

class PermissionsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Permissions
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(PermissionsInputSet, self)._set_input('AccessToken', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the profile to access. Defaults to "me" indicating the authenticated user.)
        """
        super(PermissionsInputSet, self)._set_input('ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(PermissionsInputSet, self)._set_input('ResponseFormat', value)

class PermissionsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Permissions Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class PermissionsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PermissionsResultSet(response, path)
