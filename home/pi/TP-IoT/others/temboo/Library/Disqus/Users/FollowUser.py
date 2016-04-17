# -*- coding: utf-8 -*-

###############################################################################
#
# FollowUser
# Follows the specified user.
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

class FollowUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FollowUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FollowUser, self).__init__(temboo_session, '/Library/Disqus/Users/FollowUser')


    def new_input_set(self):
        return FollowUserInputSet()

    def _make_result_set(self, result, path):
        return FollowUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FollowUserChoreographyExecution(session, exec_id, path)

class FollowUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FollowUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth 2.0 access token.)
        """
        super(FollowUserInputSet, self)._set_input('AccessToken', value)
    def set_Callback(self, value):
        """
        Set the value of the Callback input for this Choreo. ((optional, string) The name of a callback function to wrap the response in. Used when setting ResponseFormat to "jsonp".)
        """
        super(FollowUserInputSet, self)._set_input('Callback', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        super(FollowUserInputSet, self)._set_input('PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and jsonp.)
        """
        super(FollowUserInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((conditional, string) The User ID that is to be followed. If UserID is set, then Username must be null.)
        """
        super(FollowUserInputSet, self)._set_input('UserID', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) The Disqus username that is to be followed.  If Username is being set, then UserID must be null.)
        """
        super(FollowUserInputSet, self)._set_input('Username', value)


class FollowUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FollowUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class FollowUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FollowUserResultSet(response, path)
