# -*- coding: utf-8 -*-

###############################################################################
#
# CountIncidents
# Returns a count of incidents that match a specified criteria.
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

class CountIncidents(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CountIncidents Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CountIncidents, self).__init__(temboo_session, '/Library/PagerDuty/Incidents/CountIncidents')


    def new_input_set(self):
        return CountIncidentsInputSet()

    def _make_result_set(self, result, path):
        return CountIncidentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CountIncidentsChoreographyExecution(session, exec_id, path)

class CountIncidentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CountIncidents
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by PagerDuty.)
        """
        super(CountIncidentsInputSet, self)._set_input('APIKey', value)
    def set_AssignedToUser(self, value):
        """
        Set the value of the AssignedToUser input for this Choreo. ((optional, string) Returns the count of incidents assigned to the specified user.)
        """
        super(CountIncidentsInputSet, self)._set_input('AssignedToUser', value)
    def set_DateRange(self, value):
        """
        Set the value of the DateRange input for this Choreo. ((optional, string) When set to "all", this allows you to retrieve the count of all incidents since the account was created.)
        """
        super(CountIncidentsInputSet, self)._set_input('DateRange', value)
    def set_IncidentKey(self, value):
        """
        Set the value of the IncidentKey input for this Choreo. ((optional, string) Returns the count of incidents with the specified key.)
        """
        super(CountIncidentsInputSet, self)._set_input('IncidentKey', value)
    def set_Service(self, value):
        """
        Set the value of the Service input for this Choreo. ((optional, string) Returns the count of incidents associated with the specified service.)
        """
        super(CountIncidentsInputSet, self)._set_input('Service', value)
    def set_Since(self, value):
        """
        Set the value of the Since input for this Choreo. ((optional, date) The start of the date range to search (e.g., 2013-03-06T15:28-05). Note that including the time is optional.)
        """
        super(CountIncidentsInputSet, self)._set_input('Since', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((optional, string) Returns the count of incidents with this specified status. Valid values are: triggered, acknowledged, and resolved.)
        """
        super(CountIncidentsInputSet, self)._set_input('Status', value)
    def set_SubDomain(self, value):
        """
        Set the value of the SubDomain input for this Choreo. ((required, string) The subdomain of your PagerDuty site address.)
        """
        super(CountIncidentsInputSet, self)._set_input('SubDomain', value)
    def set_Until(self, value):
        """
        Set the value of the Until input for this Choreo. ((optional, date) The end of the date range to search (e.g., 2013-03-06T15:28-05). Note that including the time is optional.)
        """
        super(CountIncidentsInputSet, self)._set_input('Until', value)

class CountIncidentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CountIncidents Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PagerDuty.)
        """
        return self._output.get('Response', None)

class CountIncidentsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CountIncidentsResultSet(response, path)
