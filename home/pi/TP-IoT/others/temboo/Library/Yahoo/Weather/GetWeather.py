# -*- coding: utf-8 -*-

###############################################################################
#
# GetWeather
# Retrieves the Yahoo Weather RSS Feed for any specified location by WOEID.
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

class GetWeather(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetWeather Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetWeather, self).__init__(temboo_session, '/Library/Yahoo/Weather/GetWeather')


    def new_input_set(self):
        return GetWeatherInputSet()

    def _make_result_set(self, result, path):
        return GetWeatherResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWeatherChoreographyExecution(session, exec_id, path)

class GetWeatherInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetWeather
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Day(self, value):
        """
        Set the value of the Day input for this Choreo. ((optional, integer) An index in the range 1 to 5 that corresponds to the forecast day you want to retrieve. Today corresponds to 1, tomorrow corresponds to 2, and so on. Defaults to 1.)
        """
        super(GetWeatherInputSet, self)._set_input('Day', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(GetWeatherInputSet, self)._set_input('ResponseFormat', value)
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((optional, string) The unit of temperature in the response. Acceptable inputs: f for Fahrenheit or c for Celsius. Defaults to f. When c is specified, all units measurements returned are changed to metric.)
        """
        super(GetWeatherInputSet, self)._set_input('Units', value)
    def set_WOEID(self, value):
        """
        Set the value of the WOEID input for this Choreo. ((required, integer) Where On Earth ID for the desired location. This unique integer can be found by first running the GetWeatherByCoordinates Choreo.)
        """
        super(GetWeatherInputSet, self)._set_input('WOEID', value)

class GetWeatherResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetWeather Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Yahoo Weather.)
        """
        return self._output.get('Response', None)
    def get_ConditionCode(self):
        """
        Retrieve the value for the "ConditionCode" output from this Choreo execution. ((integer) A code representing the current condition.)
        """
        return self._output.get('ConditionCode', None)
    def get_ConditionText(self):
        """
        Retrieve the value for the "ConditionText" output from this Choreo execution. ((string) The textual description for the current condition.)
        """
        return self._output.get('ConditionText', None)
    def get_ForecastCode(self):
        """
        Retrieve the value for the "ForecastCode" output from this Choreo execution. ((integer) A code representing the forecast condition.)
        """
        return self._output.get('ForecastCode', None)
    def get_ForecastText(self):
        """
        Retrieve the value for the "ForecastText" output from this Choreo execution. ((string) The textual description for the specified day's forecast condition.)
        """
        return self._output.get('ForecastText', None)
    def get_High(self):
        """
        Retrieve the value for the "High" output from this Choreo execution. ((integer) The high temperature forecast for the specified day.)
        """
        return self._output.get('High', None)
    def get_Humidity(self):
        """
        Retrieve the value for the "Humidity" output from this Choreo execution. ((decimal) The current measurement for atmospheric humidity.)
        """
        return self._output.get('Humidity', None)
    def get_Low(self):
        """
        Retrieve the value for the "Low" output from this Choreo execution. ((integer) The low temperature forecast for the specified day.)
        """
        return self._output.get('Low', None)
    def get_Pressure(self):
        """
        Retrieve the value for the "Pressure" output from this Choreo execution. ((decimal) The current measurement for atmospheric pressure.)
        """
        return self._output.get('Pressure', None)
    def get_Temperature(self):
        """
        Retrieve the value for the "Temperature" output from this Choreo execution. ((integer) The current temperature.)
        """
        return self._output.get('Temperature', None)
    def get_Visibility(self):
        """
        Retrieve the value for the "Visibility" output from this Choreo execution. ((decimal) The current measurement for visibility.)
        """
        return self._output.get('Visibility', None)

class GetWeatherChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetWeatherResultSet(response, path)
