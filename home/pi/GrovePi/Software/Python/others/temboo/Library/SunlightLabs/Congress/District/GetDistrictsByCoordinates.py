# -*- coding: utf-8 -*-

###############################################################################
#
# GetDistrictsByCoordinates
# Returns the district that a set of latitude/longitude coordinates falls within.
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

class GetDistrictsByCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetDistrictsByCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetDistrictsByCoordinates, self).__init__(temboo_session, '/Library/SunlightLabs/Congress/District/GetDistrictsByCoordinates')


    def new_input_set(self):
        return GetDistrictsByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return GetDistrictsByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDistrictsByCoordinatesChoreographyExecution(session, exec_id, path)

class GetDistrictsByCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetDistrictsByCoordinates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        super(GetDistrictsByCoordinatesInputSet, self)._set_input('APIKey', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude coordinate of the area that a legislator represents.)
        """
        super(GetDistrictsByCoordinatesInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude coordinate of the area that a legislator represents.)
        """
        super(GetDistrictsByCoordinatesInputSet, self)._set_input('Longitude', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetDistrictsByCoordinatesInputSet, self)._set_input('ResponseFormat', value)

class GetDistrictsByCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetDistrictsByCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the Sunlight Congress API.)
        """
        return self._output.get('Response', None)

class GetDistrictsByCoordinatesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetDistrictsByCoordinatesResultSet(response, path)
