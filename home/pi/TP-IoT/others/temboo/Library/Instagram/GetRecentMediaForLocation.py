# -*- coding: utf-8 -*-

###############################################################################
#
# GetRecentMediaForLocation
# Retrieves a list of recent media objects from a given location.
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

class GetRecentMediaForLocation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRecentMediaForLocation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetRecentMediaForLocation, self).__init__(temboo_session, '/Library/Instagram/GetRecentMediaForLocation')


    def new_input_set(self):
        return GetRecentMediaForLocationInputSet()

    def _make_result_set(self, result, path):
        return GetRecentMediaForLocationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecentMediaForLocationChoreographyExecution(session, exec_id, path)

class GetRecentMediaForLocationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRecentMediaForLocation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The access token retrieved during the OAuth 2.0 process. Required unless you provide the ClientID.)
        """
        super(GetRecentMediaForLocationInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide an AccessToken.)
        """
        super(GetRecentMediaForLocationInputSet, self)._set_input('ClientID', value)
    def set_LocationID(self, value):
        """
        Set the value of the LocationID input for this Choreo. ((required, integer) The ID for the location that you want to retrieve information for.)
        """
        super(GetRecentMediaForLocationInputSet, self)._set_input('LocationID', value)
    def set_MaxID(self, value):
        """
        Set the value of the MaxID input for this Choreo. ((optional, string) Returns media after this max_id.)
        """
        super(GetRecentMediaForLocationInputSet, self)._set_input('MaxID', value)
    def set_MaxTimestamp(self, value):
        """
        Set the value of the MaxTimestamp input for this Choreo. ((optional, date) Returns media before this UNIX timestamp.)
        """
        super(GetRecentMediaForLocationInputSet, self)._set_input('MaxTimestamp', value)
    def set_MinID(self, value):
        """
        Set the value of the MinID input for this Choreo. ((optional, string) Returns media before this min_id.)
        """
        super(GetRecentMediaForLocationInputSet, self)._set_input('MinID', value)
    def set_MinTimestamp(self, value):
        """
        Set the value of the MinTimestamp input for this Choreo. ((optional, date) Returns media after this UNIX timestamp.)
        """
        super(GetRecentMediaForLocationInputSet, self)._set_input('MinTimestamp', value)

class GetRecentMediaForLocationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRecentMediaForLocation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class GetRecentMediaForLocationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetRecentMediaForLocationResultSet(response, path)
