# -*- coding: utf-8 -*-

###############################################################################
#
# Account
# Retrieves the account information for the user associated with the given authorized access token.
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

class Account(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Account Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Account, self).__init__(temboo_session, '/Library/Dwolla/Users/Account')


    def new_input_set(self):
        return AccountInputSet()

    def _make_result_set(self, result, path):
        return AccountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AccountChoreographyExecution(session, exec_id, path)

class AccountInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Account
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth token.)
        """
        super(AccountInputSet, self)._set_input('AccessToken', value)

class AccountResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Account Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class AccountChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AccountResultSet(response, path)
