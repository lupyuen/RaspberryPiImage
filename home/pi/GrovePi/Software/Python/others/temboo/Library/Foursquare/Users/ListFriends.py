# -*- coding: utf-8 -*-

###############################################################################
#
# ListFriends
# Retrieve a list of a user's friends.
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

class ListFriends(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListFriends Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListFriends, self).__init__(temboo_session, '/Library/Foursquare/Users/ListFriends')


    def new_input_set(self):
        return ListFriendsInputSet()

    def _make_result_set(self, result, path):
        return ListFriendsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListFriendsChoreographyExecution(session, exec_id, path)

class ListFriendsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListFriends
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results returned, up to 500.)
        """
        super(ListFriendsInputSet, self)._set_input('Limit', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API Oauth token string.)
        """
        super(ListFriendsInputSet, self)._set_input('OauthToken', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Specify an offest to page through results.)
        """
        super(ListFriendsInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(ListFriendsInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) Identity of the user to get friends for. Defaults to "self" to get lists of the acting user.)
        """
        super(ListFriendsInputSet, self)._set_input('UserID', value)

class ListFriendsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListFriends Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class ListFriendsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListFriendsResultSet(response, path)
