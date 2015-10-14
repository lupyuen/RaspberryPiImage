# -*- coding: utf-8 -*-

###############################################################################
#
# SearchUsers
# Allows you to search for users using CloudMine's search query language syntax.
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

class SearchUsers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchUsers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchUsers, self).__init__(temboo_session, '/Library/CloudMine/UserAccountManagement/SearchUsers')


    def new_input_set(self):
        return SearchUsersInputSet()

    def _make_result_set(self, result, path):
        return SearchUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchUsersChoreographyExecution(session, exec_id, path)

class SearchUsersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchUsers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        super(SearchUsersInputSet, self)._set_input('APIKey', value)
    def set_ApplicationIdentifier(self, value):
        """
        Set the value of the ApplicationIdentifier input for this Choreo. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        super(SearchUsersInputSet, self)._set_input('ApplicationIdentifier', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) Search query for which users to retrieve.)
        """
        super(SearchUsersInputSet, self)._set_input('Query', value)
    def set_SessionToken(self, value):
        """
        Set the value of the SessionToken input for this Choreo. ((required, string) The session token for an existing user (returned by the AccountLogin Choreo).)
        """
        super(SearchUsersInputSet, self)._set_input('SessionToken', value)

class SearchUsersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchUsers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CloudMine.)
        """
        return self._output.get('Response', None)

class SearchUsersChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchUsersResultSet(response, path)
