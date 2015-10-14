# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateProfile
# Updates values that users are able to set under "Account" tab of their settings page.
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

class UpdateProfile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateProfile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateProfile, self).__init__(temboo_session, '/Library/Twitter/Users/UpdateProfile')


    def new_input_set(self):
        return UpdateProfileInputSet()

    def _make_result_set(self, result, path):
        return UpdateProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateProfileChoreographyExecution(session, exec_id, path)

class UpdateProfileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateProfile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(UpdateProfileInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(UpdateProfileInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The API Key (or Consumer Key) provided by Twitter.)
        """
        super(UpdateProfileInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The API Secret (or Consumer Secret) provided by Twitter.)
        """
        super(UpdateProfileInputSet, self)._set_input('ConsumerSecret', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description of the user owning the account. Maximum of 160 characters.)
        """
        super(UpdateProfileInputSet, self)._set_input('Description', value)
    def set_IncludeUserEntities(self, value):
        """
        Set the value of the IncludeUserEntities input for this Choreo. ((optional, boolean) The user "entities" node containing extra metadata will not be included when set to false.)
        """
        super(UpdateProfileInputSet, self)._set_input('IncludeUserEntities', value)
    def set_Location(self, value):
        """
        Set the value of the Location input for this Choreo. ((optional, string) The city or country describing where the user of the account is located.)
        """
        super(UpdateProfileInputSet, self)._set_input('Location', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((optional, string) The full name associated with the profile. Maximum of 20 characters.)
        """
        super(UpdateProfileInputSet, self)._set_input('Name', value)
    def set_SkipStatus(self, value):
        """
        Set the value of the SkipStatus input for this Choreo. ((optional, boolean) When set to true, statuses will not be included in the returned user objects.)
        """
        super(UpdateProfileInputSet, self)._set_input('SkipStatus', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((optional, string) URL associated with the profile.)
        """
        super(UpdateProfileInputSet, self)._set_input('URL', value)

class UpdateProfileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateProfile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The rate limit ceiling for this particular request.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The number of requests left for the 15 minute window.)
        """
        return self._output.get('Remaining', None)
    def get_Reset(self):
        """
        Retrieve the value for the "Reset" output from this Choreo execution. ((date) The remaining window before the rate limit resets in UTC epoch seconds.)
        """
        return self._output.get('Reset', None)

class UpdateProfileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateProfileResultSet(response, path)
