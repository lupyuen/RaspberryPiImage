# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateIncidents
# Allows you to acknowledge, resolve, escalate or reassign one or more incidents.
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

class UpdateIncidents(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateIncidents Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateIncidents, self).__init__(temboo_session, '/Library/PagerDuty/Incidents/UpdateIncidents')


    def new_input_set(self):
        return UpdateIncidentsInputSet()

    def _make_result_set(self, result, path):
        return UpdateIncidentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateIncidentsChoreographyExecution(session, exec_id, path)

class UpdateIncidentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateIncidents
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by PagerDuty.)
        """
        super(UpdateIncidentsInputSet, self)._set_input('APIKey', value)
    def set_Incidents(self, value):
        """
        Set the value of the Incidents input for this Choreo. ((required, json) An array of incident objects that each include an incident ID. Other optional incident properties that can be present include: status, escalation_level, assigned_to_user, and escalation_policy.)
        """
        super(UpdateIncidentsInputSet, self)._set_input('Incidents', value)
    def set_RequesterID(self, value):
        """
        Set the value of the RequesterID input for this Choreo. ((required, string) The ID of the user making the request. This will be added to the incident log entry.)
        """
        super(UpdateIncidentsInputSet, self)._set_input('RequesterID', value)
    def set_SubDomain(self, value):
        """
        Set the value of the SubDomain input for this Choreo. ((required, string) The subdomain of your PagerDuty site address.)
        """
        super(UpdateIncidentsInputSet, self)._set_input('SubDomain', value)

class UpdateIncidentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateIncidents Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PagerDuty.)
        """
        return self._output.get('Response', None)

class UpdateIncidentsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateIncidentsResultSet(response, path)
