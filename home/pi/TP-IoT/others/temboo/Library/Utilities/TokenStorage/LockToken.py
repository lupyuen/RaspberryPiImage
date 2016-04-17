# -*- coding: utf-8 -*-

###############################################################################
#
# LockToken
# Locks a specified token.
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

class LockToken(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LockToken Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(LockToken, self).__init__(temboo_session, '/Library/Utilities/TokenStorage/LockToken')


    def new_input_set(self):
        return LockTokenInputSet()

    def _make_result_set(self, result, path):
        return LockTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LockTokenChoreographyExecution(session, exec_id, path)

class LockTokenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LockToken
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the token to lock.)
        """
        super(LockTokenInputSet, self)._set_input('Name', value)

class LockTokenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LockToken Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Token(self):
        """
        Retrieve the value for the "Token" output from this Choreo execution. ((string) When a lock has been obtained, the token value will be returned. If a lock can not be obtained, and empty string is returned.)
        """
        return self._output.get('Token', None)

class LockTokenChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return LockTokenResultSet(response, path)
