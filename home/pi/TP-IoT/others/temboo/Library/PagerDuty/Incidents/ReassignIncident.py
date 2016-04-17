# -*- coding: utf-8 -*-

###############################################################################
#
# ReassignIncident
# Reassigns an incident.
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

class ReassignIncident(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReassignIncident Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ReassignIncident, self).__init__(temboo_session, '/Library/PagerDuty/Incidents/ReassignIncident')


    def new_input_set(self):
        return ReassignIncidentInputSet()

    def _make_result_set(self, result, path):
        return ReassignIncidentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReassignIncidentChoreographyExecution(session, exec_id, path)

class ReassignIncidentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReassignIncident
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by PagerDuty.)
        """
        super(ReassignIncidentInputSet, self)._set_input('APIKey', value)
    def set_AssignedToUser(self, value):
        """
        Set the value of the AssignedToUser input for this Choreo. ((required, string) Assigns this incident to the specified user id.)
        """
        super(ReassignIncidentInputSet, self)._set_input('AssignedToUser', value)
    def set_EscalationLevel(self, value):
        """
        Set the value of the EscalationLevel input for this Choreo. ((optional, integer) Escalates the incident to this level in the escalation policy.)
        """
        super(ReassignIncidentInputSet, self)._set_input('EscalationLevel', value)
    def set_IncidentID(self, value):
        """
        Set the value of the IncidentID input for this Choreo. ((required, string) The ID of the incident to reassign.)
        """
        super(ReassignIncidentInputSet, self)._set_input('IncidentID', value)
    def set_RequesterID(self, value):
        """
        Set the value of the RequesterID input for this Choreo. ((required, string) The ID of the user making the request. This will be added to the incident log entry.)
        """
        super(ReassignIncidentInputSet, self)._set_input('RequesterID', value)
    def set_SubDomain(self, value):
        """
        Set the value of the SubDomain input for this Choreo. ((required, string) The subdomain of your PagerDuty site address.)
        """
        super(ReassignIncidentInputSet, self)._set_input('SubDomain', value)

class ReassignIncidentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReassignIncident Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PagerDuty.)
        """
        return self._output.get('Response', None)

class ReassignIncidentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ReassignIncidentResultSet(response, path)
