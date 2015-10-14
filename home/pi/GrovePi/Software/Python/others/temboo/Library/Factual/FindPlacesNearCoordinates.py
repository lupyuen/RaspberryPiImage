# -*- coding: utf-8 -*-

###############################################################################
#
# FindPlacesNearCoordinates
# Find places near specified latitude, longitude coordinates.
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

class FindPlacesNearCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindPlacesNearCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FindPlacesNearCoordinates, self).__init__(temboo_session, '/Library/Factual/FindPlacesNearCoordinates')


    def new_input_set(self):
        return FindPlacesNearCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return FindPlacesNearCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindPlacesNearCoordinatesChoreographyExecution(session, exec_id, path)

class FindPlacesNearCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindPlacesNearCoordinates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by Factual (AKA the OAuth Consumer Key).)
        """
        super(FindPlacesNearCoordinatesInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((optional, string) The API Secret provided by Factual (AKA the OAuth Consumer Secret).)
        """
        super(FindPlacesNearCoordinatesInputSet, self)._set_input('APISecret', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) Enter latitude coordinates of the location defining the center of the search radius.)
        """
        super(FindPlacesNearCoordinatesInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) Enter longitude coordinates of the location defining the center of the search radius.)
        """
        super(FindPlacesNearCoordinatesInputSet, self)._set_input('Longitude', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) A search string (i.e. Starbucks))
        """
        super(FindPlacesNearCoordinatesInputSet, self)._set_input('Query', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((required, integer) Provide the radius (in meters, and centered on the latitude-longitude coordinates specified) for which search results will be returned.)
        """
        super(FindPlacesNearCoordinatesInputSet, self)._set_input('Radius', value)

class FindPlacesNearCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindPlacesNearCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Factual.)
        """
        return self._output.get('Response', None)

class FindPlacesNearCoordinatesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FindPlacesNearCoordinatesResultSet(response, path)
