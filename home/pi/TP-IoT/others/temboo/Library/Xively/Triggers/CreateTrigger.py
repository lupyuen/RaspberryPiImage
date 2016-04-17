# -*- coding: utf-8 -*-

###############################################################################
#
# CreateTrigger
# Creates a new trigger.
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

class CreateTrigger(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateTrigger Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateTrigger, self).__init__(temboo_session, '/Library/Xively/Triggers/CreateTrigger')


    def new_input_set(self):
        return CreateTriggerInputSet()

    def _make_result_set(self, result, path):
        return CreateTriggerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateTriggerChoreographyExecution(session, exec_id, path)

class CreateTriggerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateTrigger
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        super(CreateTriggerInputSet, self)._set_input('APIKey', value)
    def set_DatastreamID(self, value):
        """
        Set the value of the DatastreamID input for this Choreo. ((required, string) The ID of the datastream you would like to create a trigger for.)
        """
        super(CreateTriggerInputSet, self)._set_input('DatastreamID', value)
    def set_FeedID(self, value):
        """
        Set the value of the FeedID input for this Choreo. ((required, integer) The ID of the feed you would like to create a trigger for.)
        """
        super(CreateTriggerInputSet, self)._set_input('FeedID', value)
    def set_ThresholdValue(self, value):
        """
        Set the value of the ThresholdValue input for this Choreo. ((required, string) Threshold that will cause the trigger to activate. Not required if TriggerType = "change", "frozen" or "live". Required for all others.)
        """
        super(CreateTriggerInputSet, self)._set_input('ThresholdValue', value)
    def set_TriggerType(self, value):
        """
        Set the value of the TriggerType input for this Choreo. ((required, string) Type of trigger. Possible values: "gt", "gte", "lt", "lte", "eq", "change" (any change), "frozen" (no updates for 15 minutes), or "live" (updated again after being frozen).)
        """
        super(CreateTriggerInputSet, self)._set_input('TriggerType', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((required, string) The URL that the Xively trigger will post to when activated. Ex: http://requestb.in)
        """
        super(CreateTriggerInputSet, self)._set_input('URL', value)

class CreateTriggerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateTrigger Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful trigger creation, the code should be 201.)
        """
        return self._output.get('ResponseStatusCode', None)
    def get_TriggerID(self):
        """
        Retrieve the value for the "TriggerID" output from this Choreo execution. ((integer) TriggerID extracted from the TriggerLocation.)
        """
        return self._output.get('TriggerID', None)
    def get_TriggerLocation(self):
        """
        Retrieve the value for the "TriggerLocation" output from this Choreo execution. ((string) The URL of the newly created trigger.)
        """
        return self._output.get('TriggerLocation', None)

class CreateTriggerChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateTriggerResultSet(response, path)
