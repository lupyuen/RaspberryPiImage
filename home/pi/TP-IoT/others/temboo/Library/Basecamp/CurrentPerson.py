# -*- coding: utf-8 -*-

###############################################################################
#
# CurrentPerson
# Retrieves information on the person who's credentials are specified.
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

class CurrentPerson(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CurrentPerson Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CurrentPerson, self).__init__(temboo_session, '/Library/Basecamp/CurrentPerson')


    def new_input_set(self):
        return CurrentPersonInputSet()

    def _make_result_set(self, result, path):
        return CurrentPersonResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CurrentPersonChoreographyExecution(session, exec_id, path)

class CurrentPersonInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CurrentPerson
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) The Basecamp account name for you or your company. This is the first part of your account URL.)
        """
        super(CurrentPersonInputSet, self)._set_input('AccountName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Basecamp password.  You can use the value 'X' when specifying an API Key for the Username input.)
        """
        super(CurrentPersonInputSet, self)._set_input('Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Basecamp username or API Key.)
        """
        super(CurrentPersonInputSet, self)._set_input('Username', value)

class CurrentPersonResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CurrentPerson Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Basecamp.)
        """
        return self._output.get('Response', None)

class CurrentPersonChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CurrentPersonResultSet(response, path)
