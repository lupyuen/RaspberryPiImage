# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateTrigger
# Updates an existing trigger.
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

class UpdateTrigger(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateTrigger Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateTrigger, self).__init__(temboo_session, '/Library/Xively/Triggers/UpdateTrigger')


    def new_input_set(self):
        return UpdateTriggerInputSet()

    def _make_result_set(self, result, path):
        return UpdateTriggerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateTriggerChoreographyExecution(session, exec_id, path)

class UpdateTriggerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateTrigger
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        super(UpdateTriggerInputSet, self)._set_input('APIKey', value)
    def set_ThresholdValue(self, value):
        """
        Set the value of the ThresholdValue input for this Choreo. ((optional, string) Threshold that will cause the trigger to activate. Include input only if changing Threshold Value.)
        """
        super(UpdateTriggerInputSet, self)._set_input('ThresholdValue', value)
    def set_TriggerID(self, value):
        """
        Set the value of the TriggerID input for this Choreo. ((required, integer) TriggerID for the trigger that you wish to update.)
        """
        super(UpdateTriggerInputSet, self)._set_input('TriggerID', value)
    def set_TriggerType(self, value):
        """
        Set the value of the TriggerType input for this Choreo. ((optional, string) Type of trigger. Include input only if changing TriggerType. Valid values: gt, gte, lt, lte, eq, change (any change), frozen (no updates for 15 minutes), or live (updated again after being frozen).)
        """
        super(UpdateTriggerInputSet, self)._set_input('TriggerType', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((optional, string) The URL that the Xively trigger will post to when activated. Include input only if changing the URL. Ex: http://requestb.in)
        """
        super(UpdateTriggerInputSet, self)._set_input('URL', value)

class UpdateTriggerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateTrigger Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful trigger update, the code should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class UpdateTriggerChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateTriggerResultSet(response, path)
