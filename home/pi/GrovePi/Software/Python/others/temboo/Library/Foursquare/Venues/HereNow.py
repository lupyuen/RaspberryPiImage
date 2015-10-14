# -*- coding: utf-8 -*-

###############################################################################
#
# HereNow
# Retrieves a count of how many people are at a given venue. For authenticated users, friends and friends-of-friends at the venue are also returned.
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

class HereNow(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the HereNow Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(HereNow, self).__init__(temboo_session, '/Library/Foursquare/Venues/HereNow')


    def new_input_set(self):
        return HereNowInputSet()

    def _make_result_set(self, result, path):
        return HereNowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return HereNowChoreographyExecution(session, exec_id, path)

class HereNowInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the HereNow
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AfterTimestamp(self, value):
        """
        Set the value of the AfterTimestamp input for this Choreo. ((optional, date) Retrieve the first results to follow this timestamp (an epoch timestamp in seconds).)
        """
        super(HereNowInputSet, self)._set_input('AfterTimestamp', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to return, up to 500.)
        """
        super(HereNowInputSet, self)._set_input('Limit', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(HereNowInputSet, self)._set_input('OauthToken', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used to page through results.)
        """
        super(HereNowInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(HereNowInputSet, self)._set_input('ResponseFormat', value)
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((required, string) The ID associated with the venue you want to retrieve details for.)
        """
        super(HereNowInputSet, self)._set_input('VenueID', value)

class HereNowResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the HereNow Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class HereNowChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return HereNowResultSet(response, path)
