# -*- coding: utf-8 -*-

###############################################################################
#
# GetUserInfo
# Returns information about a specified user.
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

class GetUserInfo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUserInfo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetUserInfo, self).__init__(temboo_session, '/Library/Bitly/UserInfo/GetUserInfo')


    def new_input_set(self):
        return GetUserInfoInputSet()

    def _make_result_set(self, result, path):
        return GetUserInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUserInfoChoreographyExecution(session, exec_id, path)

class GetUserInfoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUserInfo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The OAuth access token provided by Bitly.)
        """
        super(GetUserInfoInputSet, self)._set_input('AccessToken', value)
    def set_FullName(self, value):
        """
        Set the value of the FullName input for this Choreo. ((optional, string) The users full name value (only available for the authenticated user).)
        """
        super(GetUserInfoInputSet, self)._set_input('FullName', value)
    def set_Login(self, value):
        """
        Set the value of the Login input for this Choreo. ((optional, string) The Bitly login of the user whose info to look up. If not given, the authenticated user will be used.)
        """
        super(GetUserInfoInputSet, self)._set_input('Login', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Accepted values are "json" or "xml". Defaults to "json".)
        """
        super(GetUserInfoInputSet, self)._set_input('ResponseFormat', value)

class GetUserInfoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUserInfo Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Bitly.)
        """
        return self._output.get('Response', None)

class GetUserInfoChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetUserInfoResultSet(response, path)
