# -*- coding: utf-8 -*-

###############################################################################
#
# ListBugHistory
# Retrieves detailed history for a specified bug.
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

class ListBugHistory(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListBugHistory Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListBugHistory, self).__init__(temboo_session, '/Library/Bugzilla/ListBugHistory')


    def new_input_set(self):
        return ListBugHistoryInputSet()

    def _make_result_set(self, result, path):
        return ListBugHistoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListBugHistoryChoreographyExecution(session, exec_id, path)

class ListBugHistoryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListBugHistory
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BugID(self, value):
        """
        Set the value of the BugID input for this Choreo. ((required, integer) The ID for the bug to retrieve history information for.)
        """
        super(ListBugHistoryInputSet, self)._set_input('BugID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, password) Your Bugzilla password.)
        """
        super(ListBugHistoryInputSet, self)._set_input('Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((optional, string) The base URL for the Bugzilla server to access. Defaults to https://api-dev.bugzilla.mozilla.org/latest. To access the test server, set to https://api-dev.bugzilla.mozilla.org/test/latest.)
        """
        super(ListBugHistoryInputSet, self)._set_input('Server', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((optional, string) Your Bugzilla username.)
        """
        super(ListBugHistoryInputSet, self)._set_input('Username', value)

class ListBugHistoryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListBugHistory Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Bugzilla.)
        """
        return self._output.get('Response', None)

class ListBugHistoryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListBugHistoryResultSet(response, path)
