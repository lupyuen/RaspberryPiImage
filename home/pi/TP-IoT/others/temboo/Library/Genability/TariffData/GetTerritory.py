# -*- coding: utf-8 -*-

###############################################################################
#
# GetTerritory
# Returns a an individual Territory objects with a given id.
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

class GetTerritory(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTerritory Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTerritory, self).__init__(temboo_session, '/Library/Genability/TariffData/GetTerritory')


    def new_input_set(self):
        return GetTerritoryInputSet()

    def _make_result_set(self, result, path):
        return GetTerritoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTerritoryChoreographyExecution(session, exec_id, path)

class GetTerritoryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTerritory
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((conditional, string) The App ID provided by Genability.)
        """
        super(GetTerritoryInputSet, self)._set_input('AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Genability.)
        """
        super(GetTerritoryInputSet, self)._set_input('AppKey', value)
    def set_PopulateItems(self, value):
        """
        Set the value of the PopulateItems input for this Choreo. ((optional, boolean) If set to "true", returns a list of territory items for each territory in the result set.)
        """
        super(GetTerritoryInputSet, self)._set_input('PopulateItems', value)
    def set_TerritoryID(self, value):
        """
        Set the value of the TerritoryID input for this Choreo. ((required, integer) The id for the territory to retrieve. This can be retrieved in the output of the GetTerritories Choreo.)
        """
        super(GetTerritoryInputSet, self)._set_input('TerritoryID', value)

class GetTerritoryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTerritory Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class GetTerritoryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTerritoryResultSet(response, path)
