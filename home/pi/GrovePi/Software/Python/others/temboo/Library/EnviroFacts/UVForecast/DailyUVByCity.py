# -*- coding: utf-8 -*-

###############################################################################
#
# DailyUVByCity
# Retrieves EPA daily Ultraviolet (UV) Index readings in a given city.
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

class DailyUVByCity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DailyUVByCity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DailyUVByCity, self).__init__(temboo_session, '/Library/EnviroFacts/UVForecast/DailyUVByCity')


    def new_input_set(self):
        return DailyUVByCityInputSet()

    def _make_result_set(self, result, path):
        return DailyUVByCityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DailyUVByCityChoreographyExecution(session, exec_id, path)

class DailyUVByCityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DailyUVByCity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((required, string) A valid City Name in the United States.)
        """
        super(DailyUVByCityInputSet, self)._set_input('City', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Results can be retrieved in either JSON or XML. Defaults to XML.)
        """
        super(DailyUVByCityInputSet, self)._set_input('ResponseType', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((required, string) The abbreviation of the state that the city resides in.)
        """
        super(DailyUVByCityInputSet, self)._set_input('State', value)

class DailyUVByCityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DailyUVByCity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from EnviroFacts.)
        """
        return self._output.get('Response', None)

class DailyUVByCityChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DailyUVByCityResultSet(response, path)
