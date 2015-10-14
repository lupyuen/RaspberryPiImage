# -*- coding: utf-8 -*-

###############################################################################
#
# GetRecentStations
# Retrieves a list of the recent Stations listened to by this user.
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

class GetRecentStations(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRecentStations Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetRecentStations, self).__init__(temboo_session, '/Library/LastFm/User/GetRecentStations')


    def new_input_set(self):
        return GetRecentStationsInputSet()

    def _make_result_set(self, result, path):
        return GetRecentStationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecentStationsChoreographyExecution(session, exec_id, path)

class GetRecentStationsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRecentStations
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your Last.fm API Key.)
        """
        super(GetRecentStationsInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your Last.fm API Secret.)
        """
        super(GetRecentStationsInputSet, self)._set_input('APISecret', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to fetch per page. Defaults to 10. Maximum is 25.)
        """
        super(GetRecentStationsInputSet, self)._set_input('Limit', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page number to fetch. Defaults to first page.)
        """
        super(GetRecentStationsInputSet, self)._set_input('Page', value)
    def set_SessionKey(self, value):
        """
        Set the value of the SessionKey input for this Choreo. ((required, string) The session key retrieved in the last step of the authorization process.)
        """
        super(GetRecentStationsInputSet, self)._set_input('SessionKey', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The last.fm username to fetch the recent Stations of.)
        """
        super(GetRecentStationsInputSet, self)._set_input('User', value)

class GetRecentStationsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRecentStations Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetRecentStationsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetRecentStationsResultSet(response, path)
