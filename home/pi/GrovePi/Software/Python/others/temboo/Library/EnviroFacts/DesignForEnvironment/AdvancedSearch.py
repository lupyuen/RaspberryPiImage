# -*- coding: utf-8 -*-

###############################################################################
#
# AdvancedSearch
# Performs a detailed search of the EPA Design for the Environment database.
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

class AdvancedSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AdvancedSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AdvancedSearch, self).__init__(temboo_session, '/Library/EnviroFacts/DesignForEnvironment/AdvancedSearch')


    def new_input_set(self):
        return AdvancedSearchInputSet()

    def _make_result_set(self, result, path):
        return AdvancedSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AdvancedSearchChoreographyExecution(session, exec_id, path)

class AdvancedSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AdvancedSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Operator(self, value):
        """
        Set the value of the Operator input for this Choreo. ((optional, string) Default output is "=" when SearchType=sector_id or product_id, and "CONTAINING" when SearchType=partner, product, or sector. Other possible values are: "<", " >", "!=", and "BEGINNING".)
        """
        super(AdvancedSearchInputSet, self)._set_input('Operator', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((conditional, string) Response can be returned in JSON or XML. Defaults to XML.)
        """
        super(AdvancedSearchInputSet, self)._set_input('ResponseFormat', value)
    def set_RowEnd(self, value):
        """
        Set the value of the RowEnd input for this Choreo. ((optional, integer) Number 1 or greater indicates the ending row number of the results displayed. Default is 4999 when RowStart is 0. Up to 5000 entries are returned in the output.)
        """
        super(AdvancedSearchInputSet, self)._set_input('RowEnd', value)
    def set_RowStart(self, value):
        """
        Set the value of the RowStart input for this Choreo. ((optional, integer) Indicates the starting row number of the results displayed. Default is 0.)
        """
        super(AdvancedSearchInputSet, self)._set_input('RowStart', value)
    def set_SearchType(self, value):
        """
        Set the value of the SearchType input for this Choreo. ((conditional, string) Indicate either "sector", "sector_id", "partner", "product", or "product_id." Used together with SearchValue and the optional Operator input to formulate a specific search of the DfE database.)
        """
        super(AdvancedSearchInputSet, self)._set_input('SearchType', value)
    def set_SearchValue(self, value):
        """
        Set the value of the SearchValue input for this Choreo. ((conditional, integer) Indicate the product, code, or sector to search for. Used together with SearchType and the optional Operator input to create a customized search.)
        """
        super(AdvancedSearchInputSet, self)._set_input('SearchValue', value)

class AdvancedSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AdvancedSearch Choreo.
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

class AdvancedSearchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AdvancedSearchResultSet(response, path)
