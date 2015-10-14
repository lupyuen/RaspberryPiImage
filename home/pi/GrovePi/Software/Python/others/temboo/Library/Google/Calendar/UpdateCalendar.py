# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateCalendar
# Updates the metadata for a calendar.
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

class UpdateCalendar(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateCalendar Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateCalendar, self).__init__(temboo_session, '/Library/Google/Calendar/UpdateCalendar')


    def new_input_set(self):
        return UpdateCalendarInputSet()

    def _make_result_set(self, result, path):
        return UpdateCalendarResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateCalendarChoreographyExecution(session, exec_id, path)

class UpdateCalendarInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateCalendar
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(UpdateCalendarInputSet, self)._set_input('AccessToken', value)
    def set_CalendarID(self, value):
        """
        Set the value of the CalendarID input for this Choreo. ((required, string) The unique ID for the calendar to update. Note that calendar IDs can be retrieved by running GetAllCalendars or SearchCalendarsByName.)
        """
        super(UpdateCalendarInputSet, self)._set_input('CalendarID', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(UpdateCalendarInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(UpdateCalendarInputSet, self)._set_input('ClientSecret', value)
    def set_NewDescription(self, value):
        """
        Set the value of the NewDescription input for this Choreo. ((optional, string) The new description for the calendar to update.)
        """
        super(UpdateCalendarInputSet, self)._set_input('NewDescription', value)
    def set_NewLocation(self, value):
        """
        Set the value of the NewLocation input for this Choreo. ((optional, string) The new location for the calendar to update.)
        """
        super(UpdateCalendarInputSet, self)._set_input('NewLocation', value)
    def set_NewSummary(self, value):
        """
        Set the value of the NewSummary input for this Choreo. ((required, string) The new summary for the calendar to update.)
        """
        super(UpdateCalendarInputSet, self)._set_input('NewSummary', value)
    def set_NewTimezone(self, value):
        """
        Set the value of the NewTimezone input for this Choreo. ((optional, string) The new timezone for the calendar to update.)
        """
        super(UpdateCalendarInputSet, self)._set_input('NewTimezone', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(UpdateCalendarInputSet, self)._set_input('RefreshToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(UpdateCalendarInputSet, self)._set_input('ResponseFormat', value)

class UpdateCalendarResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateCalendar Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class UpdateCalendarChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateCalendarResultSet(response, path)
