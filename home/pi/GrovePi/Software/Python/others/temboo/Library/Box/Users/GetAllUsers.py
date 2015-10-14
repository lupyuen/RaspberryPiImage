# -*- coding: utf-8 -*-

###############################################################################
#
# GetAllUsers
# Returns a list of all users for the Enterprise along with their user_id, public_name, and login.
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

class GetAllUsers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAllUsers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetAllUsers, self).__init__(temboo_session, '/Library/Box/Users/GetAllUsers')


    def new_input_set(self):
        return GetAllUsersInputSet()

    def _make_result_set(self, result, path):
        return GetAllUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllUsersChoreographyExecution(session, exec_id, path)

class GetAllUsersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAllUsers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(GetAllUsersInputSet, self)._set_input('AccessToken', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(GetAllUsersInputSet, self)._set_input('AsUser', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        super(GetAllUsersInputSet, self)._set_input('Fields', value)
    def set_FilterTerm(self, value):
        """
        Set the value of the FilterTerm input for this Choreo. ((optional, string) A string used to filter the results to only users starting with the filter_term in either the name or the login.)
        """
        super(GetAllUsersInputSet, self)._set_input('FilterTerm', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of records to return.)
        """
        super(GetAllUsersInputSet, self)._set_input('Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The record at which to start. Defaults to 0.)
        """
        super(GetAllUsersInputSet, self)._set_input('Offset', value)


class GetAllUsersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAllUsers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class GetAllUsersChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetAllUsersResultSet(response, path)
