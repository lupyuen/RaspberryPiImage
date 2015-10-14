# -*- coding: utf-8 -*-

###############################################################################
#
# GetTemperature
# Retrieves the current temperature from Yahoo Weather for the specified location.
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

class GetTemperature(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTemperature Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTemperature, self).__init__(temboo_session, '/Library/Yahoo/Weather/GetTemperature')


    def new_input_set(self):
        return GetTemperatureInputSet()

    def _make_result_set(self, result, path):
        return GetTemperatureResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTemperatureChoreographyExecution(session, exec_id, path)

class GetTemperatureInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTemperature
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((required, string) The address to be searched.)
        """
        super(GetTemperatureInputSet, self)._set_input('Address', value)
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((optional, string) The unit of temperature in the response. Acceptable inputs: f for Fahrenheit or c for Celsius. Defaults to f. When c is specified, all units measurements returned are changed to metric.)
        """
        super(GetTemperatureInputSet, self)._set_input('Units', value)

class GetTemperatureResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTemperature Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Temperature(self):
        """
        Retrieve the value for the "Temperature" output from this Choreo execution. ((integer) The current temperature (defaults to Fahrenheit).)
        """
        return self._output.get('Temperature', None)

class GetTemperatureChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTemperatureResultSet(response, path)
