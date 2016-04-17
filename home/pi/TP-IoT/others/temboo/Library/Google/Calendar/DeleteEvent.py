# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteEvent
# Delete a specific event from a specified calendar.
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

class DeleteEvent(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteEvent Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteEvent, self).__init__(temboo_session, '/Library/Google/Calendar/DeleteEvent')


    def new_input_set(self):
        return DeleteEventInputSet()

    def _make_result_set(self, result, path):
        return DeleteEventResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteEventChoreographyExecution(session, exec_id, path)

class DeleteEventInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteEvent
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(DeleteEventInputSet, self)._set_input('AccessToken', value)
    def set_CalendarID(self, value):
        """
        Set the value of the CalendarID input for this Choreo. ((required, string) The unique ID for the calendar to delete. Note that calendar IDs can be retrieved by running GetAllCalendars or SearchCalendarsByName.)
        """
        super(DeleteEventInputSet, self)._set_input('CalendarID', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The name of the calendar that you want to retrieve information for. Note that if there are multiple calendars with the same name, only the first one will be returned.)
        """
        super(DeleteEventInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(DeleteEventInputSet, self)._set_input('ClientSecret', value)
    def set_EventID(self, value):
        """
        Set the value of the EventID input for this Choreo. ((required, string) The unique ID for the event to delete.)
        """
        super(DeleteEventInputSet, self)._set_input('EventID', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(DeleteEventInputSet, self)._set_input('RefreshToken', value)

class DeleteEventResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteEvent Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (No content is returned for delete calendar operations.)
        """
        return self._output.get('Response', None)
    def get_AccessToken(self):
        """
        Retrieve the value for the "AccessToken" output from this Choreo execution. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        return self._output.get('AccessToken', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class DeleteEventChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteEventResultSet(response, path)
