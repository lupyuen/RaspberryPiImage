# -*- coding: utf-8 -*-

###############################################################################
#
# GetTokenDetails
# Returns one or more tokens represented by a specified list of names.
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

class GetTokenDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTokenDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTokenDetails, self).__init__(temboo_session, '/Library/Utilities/TokenStorage/GetTokenDetails')


    def new_input_set(self):
        return GetTokenDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetTokenDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTokenDetailsChoreographyExecution(session, exec_id, path)

class GetTokenDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTokenDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Names(self, value):
        """
        Set the value of the Names input for this Choreo. ((required, json) A list of tokens to return. This should be formated as a JSON array.)
        """
        super(GetTokenDetailsInputSet, self)._set_input('Names', value)

class GetTokenDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTokenDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Tokens(self):
        """
        Retrieve the value for the "Tokens" output from this Choreo execution. ((json) The token values.)
        """
        return self._output.get('Tokens', None)

class GetTokenDetailsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTokenDetailsResultSet(response, path)
