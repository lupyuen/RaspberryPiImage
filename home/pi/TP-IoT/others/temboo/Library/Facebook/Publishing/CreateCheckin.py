# -*- coding: utf-8 -*-

###############################################################################
#
# CreateCheckin
# Creates a status update associated with  a location represented by a Page.
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

class CreateCheckin(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateCheckin Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateCheckin, self).__init__(temboo_session, '/Library/Facebook/Publishing/CreateCheckin')


    def new_input_set(self):
        return CreateCheckinInputSet()

    def _make_result_set(self, result, path):
        return CreateCheckinResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateCheckinChoreographyExecution(session, exec_id, path)

class CreateCheckinInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateCheckin
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(CreateCheckinInputSet, self)._set_input('AccessToken', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, decimal) Deprecated (retained for backward compatibility only).)
        """
        super(CreateCheckinInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((optional, decimal) Deprecated (retained for backward compatibility only).)
        """
        super(CreateCheckinInputSet, self)._set_input('Longitude', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message to include with the Checkin.)
        """
        super(CreateCheckinInputSet, self)._set_input('Message', value)
    def set_PlaceID(self, value):
        """
        Set the value of the PlaceID input for this Choreo. ((conditional, string) The ID of the place associated with your Checkin.)
        """
        super(CreateCheckinInputSet, self)._set_input('PlaceID', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the profile to create a checkin for. Defaults to "me" indicating the authenticated user.)
        """
        super(CreateCheckinInputSet, self)._set_input('ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(CreateCheckinInputSet, self)._set_input('ResponseFormat', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) A comma-separated list of user IDs of people tagged in this post.)
        """
        super(CreateCheckinInputSet, self)._set_input('Tags', value)

class CreateCheckinResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateCheckin Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class CreateCheckinChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateCheckinResultSet(response, path)
