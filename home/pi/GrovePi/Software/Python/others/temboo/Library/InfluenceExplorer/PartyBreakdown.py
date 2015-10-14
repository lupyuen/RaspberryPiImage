# -*- coding: utf-8 -*-

###############################################################################
#
# PartyBreakdown
# Returns how much an individual or organization gave to each party.
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

class PartyBreakdown(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PartyBreakdown Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PartyBreakdown, self).__init__(temboo_session, '/Library/InfluenceExplorer/PartyBreakdown')


    def new_input_set(self):
        return PartyBreakdownInputSet()

    def _make_result_set(self, result, path):
        return PartyBreakdownResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PartyBreakdownChoreographyExecution(session, exec_id, path)

class PartyBreakdownInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PartyBreakdown
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API key provided by Sunlight Data Services.)
        """
        super(PartyBreakdownInputSet, self)._set_input('APIKey', value)
    def set_ContributorType(self, value):
        """
        Set the value of the ContributorType input for this Choreo. ((required, string) This indicates whether the contributor is an individual or orgnaization. Accepted values are: "indiv" or "org". Defaults to "org".)
        """
        super(PartyBreakdownInputSet, self)._set_input('ContributorType', value)
    def set_EntityID(self, value):
        """
        Set the value of the EntityID input for this Choreo. ((required, string) The ID for the Entity that you want to return information for. This ID can be retrieved by running the SearchByName Choreo.)
        """
        super(PartyBreakdownInputSet, self)._set_input('EntityID', value)

class PartyBreakdownResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PartyBreakdown Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Influence Explorer.)
        """
        return self._output.get('Response', None)

class PartyBreakdownChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PartyBreakdownResultSet(response, path)
