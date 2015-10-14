# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByCity
# Retrieves local NPR member stations based on zip code.
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

class SearchByCity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByCity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchByCity, self).__init__(temboo_session, '/Library/NPR/StationFinder/SearchByCity')


    def new_input_set(self):
        return SearchByCityInputSet()

    def _make_result_set(self, result, path):
        return SearchByCityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByCityChoreographyExecution(session, exec_id, path)

class SearchByCityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByCity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NPR.)
        """
        super(SearchByCityInputSet, self)._set_input('APIKey', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((required, string) Enter the city name. When searching by city, the state parameter must also be specified.)
        """
        super(SearchByCityInputSet, self)._set_input('City', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are xml (the default), and json.)
        """
        super(SearchByCityInputSet, self)._set_input('ResponseFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((required, string) Enter the state. The city parameter must also be specified.)
        """
        super(SearchByCityInputSet, self)._set_input('State', value)

class SearchByCityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByCity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from NPR.)
        """
        return self._output.get('Response', None)

class SearchByCityChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchByCityResultSet(response, path)
