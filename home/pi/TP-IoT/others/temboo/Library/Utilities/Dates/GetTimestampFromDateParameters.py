# -*- coding: utf-8 -*-

###############################################################################
#
# GetTimestampFromDateParameters
# Returns the specified date parameters, expressed as the number of seconds or milliseconds since January 1, 1970 (epoch time).
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

class GetTimestampFromDateParameters(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTimestampFromDateParameters Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTimestampFromDateParameters, self).__init__(temboo_session, '/Library/Utilities/Dates/GetTimestampFromDateParameters')


    def new_input_set(self):
        return GetTimestampFromDateParametersInputSet()

    def _make_result_set(self, result, path):
        return GetTimestampFromDateParametersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTimestampFromDateParametersChoreographyExecution(session, exec_id, path)

class GetTimestampFromDateParametersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTimestampFromDateParameters
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Day(self, value):
        """
        Set the value of the Day input for this Choreo. ((conditional, integer) Sets the day (1-31) of the timestamp.)
        """
        super(GetTimestampFromDateParametersInputSet, self)._set_input('Day', value)
    def set_Granularity(self, value):
        """
        Set the value of the Granularity input for this Choreo. ((optional, string) Set to "seconds" to return the number of seconds since the epoch. Defaults to "milliseconds".)
        """
        super(GetTimestampFromDateParametersInputSet, self)._set_input('Granularity', value)
    def set_Hour(self, value):
        """
        Set the value of the Hour input for this Choreo. ((optional, integer) Sets the hours (0-23) of the timestamp.)
        """
        super(GetTimestampFromDateParametersInputSet, self)._set_input('Hour', value)
    def set_Milliseconds(self, value):
        """
        Set the value of the Milliseconds input for this Choreo. ((optional, integer) Sets the milliseconds (0-999) of the timestamp.)
        """
        super(GetTimestampFromDateParametersInputSet, self)._set_input('Milliseconds', value)
    def set_Minute(self, value):
        """
        Set the value of the Minute input for this Choreo. ((optional, integer) Sets the minutes (0-59) of the timestamp.)
        """
        super(GetTimestampFromDateParametersInputSet, self)._set_input('Minute', value)
    def set_Month(self, value):
        """
        Set the value of the Month input for this Choreo. ((conditional, integer) Sets the month (1-12) of the timestamp.)
        """
        super(GetTimestampFromDateParametersInputSet, self)._set_input('Month', value)
    def set_Second(self, value):
        """
        Set the value of the Second input for this Choreo. ((optional, integer) Sets the seconds (0-59) of the timestamp.)
        """
        super(GetTimestampFromDateParametersInputSet, self)._set_input('Second', value)
    def set_Year(self, value):
        """
        Set the value of the Year input for this Choreo. ((conditional, integer) Sets the year of the timestamp.)
        """
        super(GetTimestampFromDateParametersInputSet, self)._set_input('Year', value)

class GetTimestampFromDateParametersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTimestampFromDateParameters Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Timestamp(self):
        """
        Retrieve the value for the "Timestamp" output from this Choreo execution. ((date) A number representing the specified date and time, expressed as the number of seconds or milliseconds since January 1, 1970. The Granularity input is used to indicate seconds or milliseconds.)
        """
        return self._output.get('Timestamp', None)

class GetTimestampFromDateParametersChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTimestampFromDateParametersResultSet(response, path)
