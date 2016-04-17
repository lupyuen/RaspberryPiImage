# -*- coding: utf-8 -*-

###############################################################################
#
# ChemicalSearch
# Retrieves information about specific chemicals released by EPA-regulated facilities.
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

class ChemicalSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ChemicalSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ChemicalSearch, self).__init__(temboo_session, '/Library/EnviroFacts/Toxins/ChemicalSearch')


    def new_input_set(self):
        return ChemicalSearchInputSet()

    def _make_result_set(self, result, path):
        return ChemicalSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ChemicalSearchChoreographyExecution(session, exec_id, path)

class ChemicalSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ChemicalSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ChemicalID(self, value):
        """
        Set the value of the ChemicalID input for this Choreo. ((required, string) EPA ID number of a chemical. Chemical IDs from a given facility can be found by first running the ChemActivityByFacility or ToxinReleaseByFacility Choreos.)
        """
        super(ChemicalSearchInputSet, self)._set_input('ChemicalID', value)

class ChemicalSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ChemicalSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from EnviroFacts.)
        """
        return self._output.get('Response', None)

class ChemicalSearchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ChemicalSearchResultSet(response, path)
