# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveToken
# Retrieves a specified token.
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

class RetrieveToken(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveToken Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveToken, self).__init__(temboo_session, '/Library/Utilities/TokenStorage/RetrieveToken')


    def new_input_set(self):
        return RetrieveTokenInputSet()

    def _make_result_set(self, result, path):
        return RetrieveTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveTokenChoreographyExecution(session, exec_id, path)

class RetrieveTokenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveToken
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_LockToken(self, value):
        """
        Set the value of the LockToken input for this Choreo. ((optional, boolean) If set to true, the Choreo will attempt to lock the token after retrieving it. If the token is already locked, the Choreo will attempt to get the lock for up-to 1 minute.)
        """
        super(RetrieveTokenInputSet, self)._set_input('LockToken', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the token to retrieve.)
        """
        super(RetrieveTokenInputSet, self)._set_input('Name', value)

class RetrieveTokenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveToken Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Token(self):
        """
        Retrieve the value for the "Token" output from this Choreo execution. ((string) The token value. This will return an empty string if there is no token or if the token has expired.)
        """
        return self._output.get('Token', None)
    def get_Locked(self):
        """
        Retrieve the value for the "Locked" output from this Choreo execution. ((boolean) Returns true or false depending on whether the token is locked or not.)
        """
        return self._output.get('Locked', None)
    def get_Valid(self):
        """
        Retrieve the value for the "Valid" output from this Choreo execution. ((boolean) Returns true or false depending on whether the token is valid or not.)
        """
        return self._output.get('Valid', None)

class RetrieveTokenChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveTokenResultSet(response, path)
