# -*- coding: utf-8 -*-

###############################################################################
#
# GetPricingByPrefix
# Retrieve Nexmo's outbound pricing for the specified international prefix.
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

class GetPricingByPrefix(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPricingByPrefix Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetPricingByPrefix, self).__init__(temboo_session, '/Library/Nexmo/Account/GetPricingByPrefix')


    def new_input_set(self):
        return GetPricingByPrefixInputSet()

    def _make_result_set(self, result, path):
        return GetPricingByPrefixResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPricingByPrefixChoreographyExecution(session, exec_id, path)

class GetPricingByPrefixInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPricingByPrefix
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your API Key provided to you by Nexmo.)
        """
        super(GetPricingByPrefixInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your API Secret provided to you by Nexmo.)
        """
        super(GetPricingByPrefixInputSet, self)._set_input('APISecret', value)
    def set_Prefix(self, value):
        """
        Set the value of the Prefix input for this Choreo. ((required, integer) International dialing code. (e.g. 44))
        """
        super(GetPricingByPrefixInputSet, self)._set_input('Prefix', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        super(GetPricingByPrefixInputSet, self)._set_input('ResponseFormat', value)

class GetPricingByPrefixResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPricingByPrefix Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class GetPricingByPrefixChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetPricingByPrefixResultSet(response, path)
