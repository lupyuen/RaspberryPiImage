# -*- coding: utf-8 -*-

###############################################################################
#
# PasswordReset
# Allows a user who has forgotten their password to trigger a password reset email.
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

class PasswordReset(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PasswordReset Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PasswordReset, self).__init__(temboo_session, '/Library/CloudMine/UserAccountManagement/PasswordReset')


    def new_input_set(self):
        return PasswordResetInputSet()

    def _make_result_set(self, result, path):
        return PasswordResetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PasswordResetChoreographyExecution(session, exec_id, path)

class PasswordResetInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PasswordReset
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        super(PasswordResetInputSet, self)._set_input('APIKey', value)
    def set_ApplicationIdentifier(self, value):
        """
        Set the value of the ApplicationIdentifier input for this Choreo. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        super(PasswordResetInputSet, self)._set_input('ApplicationIdentifier', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The username/email for the user that needs to reset their password.)
        """
        super(PasswordResetInputSet, self)._set_input('Username', value)

class PasswordResetResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PasswordReset Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CloudMine.)
        """
        return self._output.get('Response', None)

class PasswordResetChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PasswordResetResultSet(response, path)
