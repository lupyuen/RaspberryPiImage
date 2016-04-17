# -*- coding: utf-8 -*-

###############################################################################
#
# AlertsPerTime
# Returns high-level statistics about the number of alerts sent for a specified time period.
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

class AlertsPerTime(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AlertsPerTime Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AlertsPerTime, self).__init__(temboo_session, '/Library/PagerDuty/Reports/AlertsPerTime')


    def new_input_set(self):
        return AlertsPerTimeInputSet()

    def _make_result_set(self, result, path):
        return AlertsPerTimeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AlertsPerTimeChoreographyExecution(session, exec_id, path)

class AlertsPerTimeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AlertsPerTime
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by PagerDuty.)
        """
        super(AlertsPerTimeInputSet, self)._set_input('APIKey', value)
    def set_Rollup(self, value):
        """
        Set the value of the Rollup input for this Choreo. ((optional, string) Used to rollup totals by time period. Valid values are: daily, weekly, or monthly.)
        """
        super(AlertsPerTimeInputSet, self)._set_input('Rollup', value)
    def set_Since(self, value):
        """
        Set the value of the Since input for this Choreo. ((required, date) The start of the date range to search (e.g., 2013-03-06T15:28-05). Note that including the time is optional.)
        """
        super(AlertsPerTimeInputSet, self)._set_input('Since', value)
    def set_SubDomain(self, value):
        """
        Set the value of the SubDomain input for this Choreo. ((required, string) The subdomain of your PagerDuty site address.)
        """
        super(AlertsPerTimeInputSet, self)._set_input('SubDomain', value)
    def set_Until(self, value):
        """
        Set the value of the Until input for this Choreo. ((required, date) The end of the date range to search (e.g., 2013-03-06T15:28-05). Note that including the time is optional.)
        """
        super(AlertsPerTimeInputSet, self)._set_input('Until', value)

class AlertsPerTimeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AlertsPerTime Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PagerDuty.)
        """
        return self._output.get('Response', None)

class AlertsPerTimeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AlertsPerTimeResultSet(response, path)
