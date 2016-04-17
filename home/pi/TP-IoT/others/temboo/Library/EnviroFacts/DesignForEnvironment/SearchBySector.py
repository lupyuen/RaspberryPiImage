# -*- coding: utf-8 -*-

###############################################################################
#
# SearchBySector
# Looks up products by sector in the EPA Design for the Environment database
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

class SearchBySector(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchBySector Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchBySector, self).__init__(temboo_session, '/Library/EnviroFacts/DesignForEnvironment/SearchBySector')


    def new_input_set(self):
        return SearchBySectorInputSet()

    def _make_result_set(self, result, path):
        return SearchBySectorResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchBySectorChoreographyExecution(session, exec_id, path)

class SearchBySectorInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchBySector
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((conditional, string) Specify either Industrial or Consumer to retrieve a list of products that fall into either category. If a specific SectorKeyword or SectorID is given, this input is ignored.)
        """
        super(SearchBySectorInputSet, self)._set_input('Category', value)
    def set_Operator(self, value):
        """
        Set the value of the Operator input for this Choreo. ((optional, string) Default output is "CONTAINING" and does not require an operator, but users can enter "<", " >", "!=", "BEGINNING", "=" for more customized searches.)
        """
        super(SearchBySectorInputSet, self)._set_input('Operator', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((conditional, string) Response can be returned in JSON or XML. Defaults to XML.)
        """
        super(SearchBySectorInputSet, self)._set_input('ResponseFormat', value)
    def set_RowEnd(self, value):
        """
        Set the value of the RowEnd input for this Choreo. ((optional, integer) Number 1 or greater indicates the ending row number of the results displayed. Default is 4999 when RowStart is 0. Up to 5000 entries are returned in the output.)
        """
        super(SearchBySectorInputSet, self)._set_input('RowEnd', value)
    def set_RowStart(self, value):
        """
        Set the value of the RowStart input for this Choreo. ((optional, integer) Indicates the starting row number of the results displayed. Default is 0.)
        """
        super(SearchBySectorInputSet, self)._set_input('RowStart', value)
    def set_SectorID(self, value):
        """
        Set the value of the SectorID input for this Choreo. ((conditional, integer) A number representing the unique identifier for the product's sector in the EnviroFacts database.)
        """
        super(SearchBySectorInputSet, self)._set_input('SectorID', value)
    def set_SectorKeyword(self, value):
        """
        Set the value of the SectorKeyword input for this Choreo. ((conditional, string) A keyword in the name of the sector to search for. If a specific SectorID is given, this input is ignored.)
        """
        super(SearchBySectorInputSet, self)._set_input('SectorKeyword', value)

class SearchBySectorResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchBySector Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Count(self):
        """
        Retrieve the value for the "Count" output from this Choreo execution. (The total number of records returned for any given search.)
        """
        return self._output.get('Count', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from EnviroFacts.)
        """
        return self._output.get('Response', None)

class SearchBySectorChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchBySectorResultSet(response, path)
