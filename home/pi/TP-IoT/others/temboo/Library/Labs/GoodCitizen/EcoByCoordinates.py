# -*- coding: utf-8 -*-

###############################################################################
#
# EcoByCoordinates
# Returns a host of eco-conscious environmental information for a specified location based on Lattitude and Longitude inputs.
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

class EcoByCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EcoByCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(EcoByCoordinates, self).__init__(temboo_session, '/Library/Labs/GoodCitizen/EcoByCoordinates')


    def new_input_set(self):
        return EcoByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return EcoByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EcoByCoordinatesChoreographyExecution(session, exec_id, path)

class EcoByCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EcoByCoordinates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((optional, string) A JSON dictionary containing credentials for Genability. See Choreo documentation for formatting examples.)
        """
        super(EcoByCoordinatesInputSet, self)._set_input('APICredentials', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude coordinate for the user's current location.)
        """
        super(EcoByCoordinatesInputSet, self)._set_input('Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of facility records to search for in the Envirofacts database.)
        """
        super(EcoByCoordinatesInputSet, self)._set_input('Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude coordinate for the user's current location.)
        """
        super(EcoByCoordinatesInputSet, self)._set_input('Longitude', value)

class EcoByCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EcoByCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from the Eco Choreo.)
        """
        return self._output.get('Response', None)

class EcoByCoordinatesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return EcoByCoordinatesResultSet(response, path)
