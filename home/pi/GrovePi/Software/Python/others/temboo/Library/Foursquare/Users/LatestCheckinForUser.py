# -*- coding: utf-8 -*-

###############################################################################
#
# LatestCheckinForUser
# Retrieves the latest check-in for an authenticated user.
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

class LatestCheckinForUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LatestCheckinForUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(LatestCheckinForUser, self).__init__(temboo_session, '/Library/Foursquare/Users/LatestCheckinForUser')


    def new_input_set(self):
        return LatestCheckinForUserInputSet()

    def _make_result_set(self, result, path):
        return LatestCheckinForUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LatestCheckinForUserChoreographyExecution(session, exec_id, path)

class LatestCheckinForUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LatestCheckinForUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API Oauth token string.)
        """
        super(LatestCheckinForUserInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(LatestCheckinForUserInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) Only 'self' is supported at this moment by the Foursquare API. Defaults to: self.)
        """
        super(LatestCheckinForUserInputSet, self)._set_input('UserID', value)

class LatestCheckinForUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LatestCheckinForUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def get_City(self):
        """
        Retrieve the value for the "City" output from this Choreo execution. ((string) The city that the venue is located in.)
        """
        return self._output.get('City', None)
    def get_CreatedAt(self):
        """
        Retrieve the value for the "CreatedAt" output from this Choreo execution. ((date) The date associated with the user's latest check-in.)
        """
        return self._output.get('CreatedAt', None)
    def get_FormattedAddress(self):
        """
        Retrieve the value for the "FormattedAddress" output from this Choreo execution. ((string) The formatted address of the venue associated with the user's latest check-in.)
        """
        return self._output.get('FormattedAddress', None)
    def get_PostalCode(self):
        """
        Retrieve the value for the "PostalCode" output from this Choreo execution. ((integer) The postal code of the venue.)
        """
        return self._output.get('PostalCode', None)
    def get_State(self):
        """
        Retrieve the value for the "State" output from this Choreo execution. ((string) The state that the venue is located in.)
        """
        return self._output.get('State', None)
    def get_VenueID(self):
        """
        Retrieve the value for the "VenueID" output from this Choreo execution. ((string) The ID of the venue associated with the user's latest check-in.)
        """
        return self._output.get('VenueID', None)
    def get_VenueName(self):
        """
        Retrieve the value for the "VenueName" output from this Choreo execution. ((string) The name of the venue that the user last checked into.)
        """
        return self._output.get('VenueName', None)

class LatestCheckinForUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return LatestCheckinForUserResultSet(response, path)
