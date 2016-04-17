# -*- coding: utf-8 -*-

###############################################################################
#
# LocalBreakdown
# Returns a breakdown of how much of the money raised was from contributors in the politician's state versus outside the politician's state.
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

class LocalBreakdown(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LocalBreakdown Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(LocalBreakdown, self).__init__(temboo_session, '/Library/InfluenceExplorer/LocalBreakdown')


    def new_input_set(self):
        return LocalBreakdownInputSet()

    def _make_result_set(self, result, path):
        return LocalBreakdownResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LocalBreakdownChoreographyExecution(session, exec_id, path)

class LocalBreakdownInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LocalBreakdown
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API key provided by Sunlight Data Services.)
        """
        super(LocalBreakdownInputSet, self)._set_input('APIKey', value)
    def set_EntityID(self, value):
        """
        Set the value of the EntityID input for this Choreo. ((required, string) The ID for the Entity that you want to return information for. This ID can be retrieved by running the SearchByName Choreo.)
        """
        super(LocalBreakdownInputSet, self)._set_input('EntityID', value)

class LocalBreakdownResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LocalBreakdown Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Influence Explorer.)
        """
        return self._output.get('Response', None)

class LocalBreakdownChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return LocalBreakdownResultSet(response, path)
