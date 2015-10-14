# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveCardToken
# Retrieves a card token based on a given id.
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

class RetrieveCardToken(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveCardToken Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveCardToken, self).__init__(temboo_session, '/Library/Stripe/Tokens/RetrieveCardToken')


    def new_input_set(self):
        return RetrieveCardTokenInputSet()

    def _make_result_set(self, result, path):
        return RetrieveCardTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveCardTokenChoreographyExecution(session, exec_id, path)

class RetrieveCardTokenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveCardToken
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(RetrieveCardTokenInputSet, self)._set_input('APIKey', value)
    def set_TokenID(self, value):
        """
        Set the value of the TokenID input for this Choreo. ((required, string) The unique identifier of the token you want to retrieve)
        """
        super(RetrieveCardTokenInputSet, self)._set_input('TokenID', value)

class RetrieveCardTokenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveCardToken Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class RetrieveCardTokenChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveCardTokenResultSet(response, path)
