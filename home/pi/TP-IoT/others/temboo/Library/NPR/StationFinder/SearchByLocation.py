# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByLocation
# Retrieves local NPR member stations near the specified latitude and longitude location coordinates.
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

class SearchByLocation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByLocation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchByLocation, self).__init__(temboo_session, '/Library/NPR/StationFinder/SearchByLocation')


    def new_input_set(self):
        return SearchByLocationInputSet()

    def _make_result_set(self, result, path):
        return SearchByLocationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByLocationChoreographyExecution(session, exec_id, path)

class SearchByLocationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByLocation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NPR.)
        """
        super(SearchByLocationInputSet, self)._set_input('APIKey', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude point of a station's location.)
        """
        super(SearchByLocationInputSet, self)._set_input('Latitude', value)
    def set_Lattitude(self, value):
        """
        Set the value of the Lattitude input for this Choreo. ((required, decimal) Deprecated (retained for backward compatibility only).)
        """
        super(SearchByLocationInputSet, self)._set_input('Lattitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude point of a station's location.)
        """
        super(SearchByLocationInputSet, self)._set_input('Longitude', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are xml (the default), and json.)
        """
        super(SearchByLocationInputSet, self)._set_input('ResponseFormat', value)

class SearchByLocationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByLocation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from NPR.)
        """
        return self._output.get('Response', None)

class SearchByLocationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchByLocationResultSet(response, path)
