# -*- coding: utf-8 -*-

###############################################################################
#
# GetUpdatedPropertyDetails
# Retrieve detailed property information that has been edited by the home's owner or agent.
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

class GetUpdatedPropertyDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUpdatedPropertyDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetUpdatedPropertyDetails, self).__init__(temboo_session, '/Library/Zillow/GetUpdatedPropertyDetails')


    def new_input_set(self):
        return GetUpdatedPropertyDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetUpdatedPropertyDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUpdatedPropertyDetailsChoreographyExecution(session, exec_id, path)

class GetUpdatedPropertyDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUpdatedPropertyDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ZPID(self, value):
        """
        Set the value of the ZPID input for this Choreo. ((required, integer) Enter a Zillow Property ID for the property being queried.)
        """
        super(GetUpdatedPropertyDetailsInputSet, self)._set_input('ZPID', value)
    def set_ZWSID(self, value):
        """
        Set the value of the ZWSID input for this Choreo. ((required, string) Enter a Zillow Web Service Identifier (ZWS ID).)
        """
        super(GetUpdatedPropertyDetailsInputSet, self)._set_input('ZWSID', value)

class GetUpdatedPropertyDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUpdatedPropertyDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Zillow.)
        """
        return self._output.get('Response', None)

class GetUpdatedPropertyDetailsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetUpdatedPropertyDetailsResultSet(response, path)
