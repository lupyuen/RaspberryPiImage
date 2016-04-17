# -*- coding: utf-8 -*-

###############################################################################
#
# StateFederalBreakdown
# Returns the portion of contribution given by an individual or organization that went to state versus federal candidates.
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

class StateFederalBreakdown(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the StateFederalBreakdown Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(StateFederalBreakdown, self).__init__(temboo_session, '/Library/InfluenceExplorer/StateFederalBreakdown')


    def new_input_set(self):
        return StateFederalBreakdownInputSet()

    def _make_result_set(self, result, path):
        return StateFederalBreakdownResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StateFederalBreakdownChoreographyExecution(session, exec_id, path)

class StateFederalBreakdownInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the StateFederalBreakdown
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API key provided by Sunlight Data Services.)
        """
        super(StateFederalBreakdownInputSet, self)._set_input('APIKey', value)
    def set_EntityID(self, value):
        """
        Set the value of the EntityID input for this Choreo. ((required, string) The ID for the Entity that you want to return information for. This ID can be retrieved by running the SearchByName Choreo.)
        """
        super(StateFederalBreakdownInputSet, self)._set_input('EntityID', value)

class StateFederalBreakdownResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the StateFederalBreakdown Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Influence Explorer.)
        """
        return self._output.get('Response', None)

class StateFederalBreakdownChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return StateFederalBreakdownResultSet(response, path)
