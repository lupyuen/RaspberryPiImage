# -*- coding: utf-8 -*-

###############################################################################
#
# GetTimeOfUseGroupIntervals
# Returns all the Intervals for a Time of Use Group within a given date range.
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

class GetTimeOfUseGroupIntervals(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTimeOfUseGroupIntervals Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTimeOfUseGroupIntervals, self).__init__(temboo_session, '/Library/Genability/TariffData/GetTimeOfUseGroupIntervals')


    def new_input_set(self):
        return GetTimeOfUseGroupIntervalsInputSet()

    def _make_result_set(self, result, path):
        return GetTimeOfUseGroupIntervalsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTimeOfUseGroupIntervalsChoreographyExecution(session, exec_id, path)

class GetTimeOfUseGroupIntervalsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTimeOfUseGroupIntervals
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The App ID provided by Genability.)
        """
        super(GetTimeOfUseGroupIntervalsInputSet, self)._set_input('AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Genability.)
        """
        super(GetTimeOfUseGroupIntervalsInputSet, self)._set_input('AppKey', value)
    def set_FromDateTime(self, value):
        """
        Set the value of the FromDateTime input for this Choreo. ((optional, date) The starting date and time of the requested Intervals (in ISO 8601 format). Defaults to current date if not specified.)
        """
        super(GetTimeOfUseGroupIntervalsInputSet, self)._set_input('FromDateTime', value)
    def set_LSEID(self, value):
        """
        Set the value of the LSEID input for this Choreo. ((required, integer) Used to retrieve a TOU Group for a specific LSE.)
        """
        super(GetTimeOfUseGroupIntervalsInputSet, self)._set_input('LSEID', value)
    def set_PageCount(self, value):
        """
        Set the value of the PageCount input for this Choreo. ((optional, integer) The number of results to return. Defaults to 25.)
        """
        super(GetTimeOfUseGroupIntervalsInputSet, self)._set_input('PageCount', value)
    def set_PageStart(self, value):
        """
        Set the value of the PageStart input for this Choreo. ((optional, integer) The page number to begin the result set from. Defaults to 1.)
        """
        super(GetTimeOfUseGroupIntervalsInputSet, self)._set_input('PageStart', value)
    def set_TOUGroupID(self, value):
        """
        Set the value of the TOUGroupID input for this Choreo. ((required, integer) Used to retrieve a TOU Group by its ID.)
        """
        super(GetTimeOfUseGroupIntervalsInputSet, self)._set_input('TOUGroupID', value)
    def set_ToDateTime(self, value):
        """
        Set the value of the ToDateTime input for this Choreo. ((optional, date) The ending date and time of the requested Intervals (in ISO 8601 format). If not specified, defaults to one week ahead of the current date.)
        """
        super(GetTimeOfUseGroupIntervalsInputSet, self)._set_input('ToDateTime', value)

class GetTimeOfUseGroupIntervalsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTimeOfUseGroupIntervals Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class GetTimeOfUseGroupIntervalsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTimeOfUseGroupIntervalsResultSet(response, path)
