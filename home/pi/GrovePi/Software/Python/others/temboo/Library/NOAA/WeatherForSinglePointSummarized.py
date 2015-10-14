# -*- coding: utf-8 -*-

###############################################################################
#
# WeatherForSinglePointSummarized
# Retrieve weather information for a single point defined by latitude and longitude coordinates.
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

class WeatherForSinglePointSummarized(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the WeatherForSinglePointSummarized Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(WeatherForSinglePointSummarized, self).__init__(temboo_session, '/Library/NOAA/WeatherForSinglePointSummarized')


    def new_input_set(self):
        return WeatherForSinglePointSummarizedInputSet()

    def _make_result_set(self, result, path):
        return WeatherForSinglePointSummarizedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WeatherForSinglePointSummarizedChoreographyExecution(session, exec_id, path)

class WeatherForSinglePointSummarizedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the WeatherForSinglePointSummarized
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((required, string) Specify a timespan for which NDFD data will be summarized. Enter: 24 hourly, for a 24 hour summary, or: 12 hourly, for a 12 hour weather summary.)
        """
        super(WeatherForSinglePointSummarizedInputSet, self)._set_input('Format', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) Enter the latitude coordinates of the point for which weather data is requested. North latitude is positive.)
        """
        super(WeatherForSinglePointSummarizedInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) Enter the longitude coordinate of the point for which weather data is requested. West longitude is negative.)
        """
        super(WeatherForSinglePointSummarizedInputSet, self)._set_input('Longitude', value)
    def set_NumberOfDays(self, value):
        """
        Set the value of the NumberOfDays input for this Choreo. ((optional, integer) Specify the number of days to retieve data for. If null, data from the earliest date in the dabase is returned.)
        """
        super(WeatherForSinglePointSummarizedInputSet, self)._set_input('NumberOfDays', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, date) Enter the start time for retrieval of NDWD information in UTC format. If null, the earliest date in the database is returned. Format: 2004-04-27T12:00.)
        """
        super(WeatherForSinglePointSummarizedInputSet, self)._set_input('StartDate', value)
    def set_Unit(self, value):
        """
        Set the value of the Unit input for this Choreo. ((optional, string) Enter the unit format the data will be displayed in. Default is: e, for Standard English (U.S. Standard).  Or: m, for Metric (SI Units).)
        """
        super(WeatherForSinglePointSummarizedInputSet, self)._set_input('Unit', value)

class WeatherForSinglePointSummarizedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the WeatherForSinglePointSummarized Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) Response from NDFD servers.)
        """
        return self._output.get('Response', None)

class WeatherForSinglePointSummarizedChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return WeatherForSinglePointSummarizedResultSet(response, path)
