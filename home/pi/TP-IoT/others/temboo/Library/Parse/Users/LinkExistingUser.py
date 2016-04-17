# -*- coding: utf-8 -*-

###############################################################################
#
# LinkExistingUser
# Allows your application to link an existing user with a service like Facebook or Twitter.
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

class LinkExistingUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LinkExistingUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(LinkExistingUser, self).__init__(temboo_session, '/Library/Parse/Users/LinkExistingUser')


    def new_input_set(self):
        return LinkExistingUserInputSet()

    def _make_result_set(self, result, path):
        return LinkExistingUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LinkExistingUserChoreographyExecution(session, exec_id, path)

class LinkExistingUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LinkExistingUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AuthData(self, value):
        """
        Set the value of the AuthData input for this Choreo. ((required, json) A JSON string containing the authentication data of the user you want to link with another service. See documentation for more formatting details.)
        """
        super(LinkExistingUserInputSet, self)._set_input('AuthData', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        super(LinkExistingUserInputSet, self)._set_input('ApplicationID', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The ID of the user that is being linked to another service.)
        """
        super(LinkExistingUserInputSet, self)._set_input('ObjectID', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        super(LinkExistingUserInputSet, self)._set_input('RESTAPIKey', value)
    def set_SessionToken(self, value):
        """
        Set the value of the SessionToken input for this Choreo. ((required, string) A valid Session Token. Note that Session Tokens can be retrieved by the Login and SignUp Choreos.)
        """
        super(LinkExistingUserInputSet, self)._set_input('SessionToken', value)

class LinkExistingUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LinkExistingUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class LinkExistingUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return LinkExistingUserResultSet(response, path)
