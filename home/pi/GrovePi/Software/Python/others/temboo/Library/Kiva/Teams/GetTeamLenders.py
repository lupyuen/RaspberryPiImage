# -*- coding: utf-8 -*-

###############################################################################
#
# GetTeamLenders
# Returns a list of public lenders belonging to a specific team.
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

class GetTeamLenders(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTeamLenders Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTeamLenders, self).__init__(temboo_session, '/Library/Kiva/Teams/GetTeamLenders')


    def new_input_set(self):
        return GetTeamLendersInputSet()

    def _make_result_set(self, result, path):
        return GetTeamLendersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTeamLendersChoreographyExecution(session, exec_id, path)

class GetTeamLendersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTeamLenders
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        super(GetTeamLendersInputSet, self)._set_input('AppID', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page position of results to return. Defaults to 1.)
        """
        super(GetTeamLendersInputSet, self)._set_input('Page', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Output returned can be XML or JSON. Defaults to JSON.)
        """
        super(GetTeamLendersInputSet, self)._set_input('ResponseType', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) The order by which to sort results: oldest  or newest. Defaults to newest.)
        """
        super(GetTeamLendersInputSet, self)._set_input('SortBy', value)
    def set_TeamID(self, value):
        """
        Set the value of the TeamID input for this Choreo. ((required, string) The TeamID for which to return lenders.)
        """
        super(GetTeamLendersInputSet, self)._set_input('TeamID', value)

class GetTeamLendersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTeamLenders Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Kiva.)
        """
        return self._output.get('Response', None)

class GetTeamLendersChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTeamLendersResultSet(response, path)
