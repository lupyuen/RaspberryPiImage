# -*- coding: utf-8 -*-

###############################################################################
#
# SearchNumbers
# Get available inbound numbers for a given country.
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

class SearchNumbers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchNumbers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchNumbers, self).__init__(temboo_session, '/Library/Nexmo/Search/SearchNumbers')


    def new_input_set(self):
        return SearchNumbersInputSet()

    def _make_result_set(self, result, path):
        return SearchNumbersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchNumbersChoreographyExecution(session, exec_id, path)

class SearchNumbersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchNumbers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your API Key provided to you by Nexmo.)
        """
        super(SearchNumbersInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your API Secret provided to you by Nexmo.)
        """
        super(SearchNumbersInputSet, self)._set_input('APISecret', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((required, string) 2-digit country code. (e.g. CA))
        """
        super(SearchNumbersInputSet, self)._set_input('Country', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((optional, integer) Page index)
        """
        super(SearchNumbersInputSet, self)._set_input('Index', value)
    def set_Pattern(self, value):
        """
        Set the value of the Pattern input for this Choreo. ((optional, string) Pattern to match.)
        """
        super(SearchNumbersInputSet, self)._set_input('Pattern', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        super(SearchNumbersInputSet, self)._set_input('ResponseFormat', value)
    def set_Size(self, value):
        """
        Set the value of the Size input for this Choreo. ((optional, integer) Page size.)
        """
        super(SearchNumbersInputSet, self)._set_input('Size', value)

class SearchNumbersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchNumbers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class SearchNumbersChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchNumbersResultSet(response, path)
