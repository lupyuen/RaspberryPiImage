# -*- coding: utf-8 -*-

###############################################################################
#
# GetDeepSearchResults
# Retrieve comprehensive property information for a specified address. 
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

class GetDeepSearchResults(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetDeepSearchResults Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetDeepSearchResults, self).__init__(temboo_session, '/Library/Zillow/GetDeepSearchResults')


    def new_input_set(self):
        return GetDeepSearchResultsInputSet()

    def _make_result_set(self, result, path):
        return GetDeepSearchResultsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDeepSearchResultsChoreographyExecution(session, exec_id, path)

class GetDeepSearchResultsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetDeepSearchResults
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((required, string) Enter the address of the property to search.)
        """
        super(GetDeepSearchResultsInputSet, self)._set_input('Address', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((required, string) Enter a city name.)
        """
        super(GetDeepSearchResultsInputSet, self)._set_input('City', value)
    def set_RentEstimate(self, value):
        """
        Set the value of the RentEstimate input for this Choreo. ((optional, boolean) Set to 1 (true) to enable. Defaults to 0 (false).)
        """
        super(GetDeepSearchResultsInputSet, self)._set_input('RentEstimate', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((required, string) Enter a State abbreviation. If State is set, an entry for City must also be entered.)
        """
        super(GetDeepSearchResultsInputSet, self)._set_input('State', value)
    def set_ZWSID(self, value):
        """
        Set the value of the ZWSID input for this Choreo. ((required, string) Enter a Zillow Web Service Identifier (ZWS ID).)
        """
        super(GetDeepSearchResultsInputSet, self)._set_input('ZWSID', value)
    def set_Zipcode(self, value):
        """
        Set the value of the Zipcode input for this Choreo. ((required, integer) Enter a zipcode. Can be combined with or without the  City and State input variables.)
        """
        super(GetDeepSearchResultsInputSet, self)._set_input('Zipcode', value)

class GetDeepSearchResultsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetDeepSearchResults Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Zillow.)
        """
        return self._output.get('Response', None)

class GetDeepSearchResultsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetDeepSearchResultsResultSet(response, path)
