# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveUser
# Retrieves information for a specified user.
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

class RetrieveUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveUser, self).__init__(temboo_session, '/Library/Bugzilla/RetrieveUser')


    def new_input_set(self):
        return RetrieveUserInputSet()

    def _make_result_set(self, result, path):
        return RetrieveUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveUserChoreographyExecution(session, exec_id, path)

class RetrieveUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, password) Your Bugzilla password.)
        """
        super(RetrieveUserInputSet, self)._set_input('Password', value)
    def set_QueryUserID(self, value):
        """
        Set the value of the QueryUserID input for this Choreo. ((required, string) The ID of the user to retrieve information for. Valid input formats include: email address, or numeric user ID. If searching by numeric ID, authentication is requred.)
        """
        super(RetrieveUserInputSet, self)._set_input('QueryUserID', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((optional, string) The base URL for the Bugzilla server to access. Defaults to https://api-dev.bugzilla.mozilla.org/latest. To access the test server, set to https://api-dev.bugzilla.mozilla.org/test/latest.)
        """
        super(RetrieveUserInputSet, self)._set_input('Server', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((optional, string) Your Bugzilla username.)
        """
        super(RetrieveUserInputSet, self)._set_input('Username', value)

class RetrieveUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Bugzilla.)
        """
        return self._output.get('Response', None)

class RetrieveUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveUserResultSet(response, path)
