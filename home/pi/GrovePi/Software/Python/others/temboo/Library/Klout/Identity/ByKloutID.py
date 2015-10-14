# -*- coding: utf-8 -*-

###############################################################################
#
# ByKloutID
# Performs a lookup for a user's identity using a Klout ID.
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

class ByKloutID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ByKloutID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ByKloutID, self).__init__(temboo_session, '/Library/Klout/Identity/ByKloutID')


    def new_input_set(self):
        return ByKloutIDInputSet()

    def _make_result_set(self, result, path):
        return ByKloutIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByKloutIDChoreographyExecution(session, exec_id, path)

class ByKloutIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ByKloutID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Klout.)
        """
        super(ByKloutIDInputSet, self)._set_input('APIKey', value)
    def set_KloutID(self, value):
        """
        Set the value of the KloutID input for this Choreo. ((required, integer) The numeric ID for a Klout user.)
        """
        super(ByKloutIDInputSet, self)._set_input('KloutID', value)

class ByKloutIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ByKloutID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Klout.)
        """
        return self._output.get('Response', None)

class ByKloutIDChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ByKloutIDResultSet(response, path)
