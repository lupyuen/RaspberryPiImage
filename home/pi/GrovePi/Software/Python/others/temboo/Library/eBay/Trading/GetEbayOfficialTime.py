# -*- coding: utf-8 -*-

###############################################################################
#
# GetEbayOfficialTime
# Gets the official eBay system time in GMT.
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

class GetEbayOfficialTime(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetEbayOfficialTime Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetEbayOfficialTime, self).__init__(temboo_session, '/Library/eBay/Trading/GetEbayOfficialTime')


    def new_input_set(self):
        return GetEbayOfficialTimeInputSet()

    def _make_result_set(self, result, path):
        return GetEbayOfficialTimeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetEbayOfficialTimeChoreographyExecution(session, exec_id, path)

class GetEbayOfficialTimeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetEbayOfficialTime
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetEbayOfficialTimeInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((conditional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(GetEbayOfficialTimeInputSet, self)._set_input('SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(GetEbayOfficialTimeInputSet, self)._set_input('SiteID', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        super(GetEbayOfficialTimeInputSet, self)._set_input('UserToken', value)

class GetEbayOfficialTimeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetEbayOfficialTime Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class GetEbayOfficialTimeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetEbayOfficialTimeResultSet(response, path)
