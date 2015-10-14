# -*- coding: utf-8 -*-

###############################################################################
#
# CreateCalendar
# Create a new secondary calendar.
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

class CreateCalendar(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateCalendar Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateCalendar, self).__init__(temboo_session, '/Library/Google/Calendar/CreateCalendar')


    def new_input_set(self):
        return CreateCalendarInputSet()

    def _make_result_set(self, result, path):
        return CreateCalendarResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateCalendarChoreographyExecution(session, exec_id, path)

class CreateCalendarInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateCalendar
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(CreateCalendarInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(CreateCalendarInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(CreateCalendarInputSet, self)._set_input('ClientSecret', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description of the calendar.)
        """
        super(CreateCalendarInputSet, self)._set_input('Description', value)
    def set_Location(self, value):
        """
        Set the value of the Location input for this Choreo. ((optional, string) Geographic location of the calendar such as "Los Angeles" or "New York".)
        """
        super(CreateCalendarInputSet, self)._set_input('Location', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(CreateCalendarInputSet, self)._set_input('RefreshToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(CreateCalendarInputSet, self)._set_input('ResponseFormat', value)
    def set_Timezone(self, value):
        """
        Set the value of the Timezone input for this Choreo. ((optional, string) The timezone for the new calendar, such as "America/Los_Angeles". Defaults to UTC if left blank.)
        """
        super(CreateCalendarInputSet, self)._set_input('Timezone', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The name for the new calendar.)
        """
        super(CreateCalendarInputSet, self)._set_input('Title', value)

class CreateCalendarResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateCalendar Choreo.
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

class CreateCalendarChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateCalendarResultSet(response, path)
