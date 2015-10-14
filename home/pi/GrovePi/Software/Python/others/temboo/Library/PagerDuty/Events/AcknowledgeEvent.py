# -*- coding: utf-8 -*-

###############################################################################
#
# AcknowledgeEvent
# Updates the state of an incident to "acknowleged", and allows you to log data to an incident log.
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

class AcknowledgeEvent(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AcknowledgeEvent Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AcknowledgeEvent, self).__init__(temboo_session, '/Library/PagerDuty/Events/AcknowledgeEvent')


    def new_input_set(self):
        return AcknowledgeEventInputSet()

    def _make_result_set(self, result, path):
        return AcknowledgeEventResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AcknowledgeEventChoreographyExecution(session, exec_id, path)

class AcknowledgeEventInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AcknowledgeEvent
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A short description that will appear in the incident's log associated with this event.)
        """
        super(AcknowledgeEventInputSet, self)._set_input('Description', value)
    def set_Details(self, value):
        """
        Set the value of the Details input for this Choreo. ((optional, json) A JSON object containing any data you'd like included in the incident log.)
        """
        super(AcknowledgeEventInputSet, self)._set_input('Details', value)
    def set_IncidentKey(self, value):
        """
        Set the value of the IncidentKey input for this Choreo. ((required, string) Identifies the incident to acknowledge.)
        """
        super(AcknowledgeEventInputSet, self)._set_input('IncidentKey', value)
    def set_ServiceKey(self, value):
        """
        Set the value of the ServiceKey input for this Choreo. ((required, string) The service key of one of your "Generic API" services. This is listed on a Generic API's service detail page.)
        """
        super(AcknowledgeEventInputSet, self)._set_input('ServiceKey', value)

class AcknowledgeEventResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AcknowledgeEvent Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PagerDuty.)
        """
        return self._output.get('Response', None)

class AcknowledgeEventChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AcknowledgeEventResultSet(response, path)
