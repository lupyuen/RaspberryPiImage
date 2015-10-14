# -*- coding: utf-8 -*-

###############################################################################
#
# ListCityCoordinatesUnsummarized
# Retrieve unsummarized latitude and longitude data for a specified list of cities.
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

class ListCityCoordinatesUnsummarized(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListCityCoordinatesUnsummarized Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListCityCoordinatesUnsummarized, self).__init__(temboo_session, '/Library/NOAA/ListCityCoordinatesUnsummarized')


    def new_input_set(self):
        return ListCityCoordinatesUnsummarizedInputSet()

    def _make_result_set(self, result, path):
        return ListCityCoordinatesUnsummarizedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListCityCoordinatesUnsummarizedChoreographyExecution(session, exec_id, path)

class ListCityCoordinatesUnsummarizedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListCityCoordinatesUnsummarized
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CitiesLevel(self, value):
        """
        Set the value of the CitiesLevel input for this Choreo. ((integer) Enter a city grouping number to retrieve its latitude and longitude coordinates. For example: enter 1, to obtain information for primary U.S. cities.)
        """
        super(ListCityCoordinatesUnsummarizedInputSet, self)._set_input('CitiesLevel', value)

class ListCityCoordinatesUnsummarizedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListCityCoordinatesUnsummarized Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) Response from NDFD servers.)
        """
        return self._output.get('Response', None)

class ListCityCoordinatesUnsummarizedChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListCityCoordinatesUnsummarizedResultSet(response, path)
