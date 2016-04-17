# -*- coding: utf-8 -*-

###############################################################################
#
# ResetPassword
# Reset a SendGrid account password.
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

class ResetPassword(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ResetPassword Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ResetPassword, self).__init__(temboo_session, '/Library/SendGrid/WebAPI/Profile/ResetPassword')


    def new_input_set(self):
        return ResetPasswordInputSet()

    def _make_result_set(self, result, path):
        return ResetPasswordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ResetPasswordChoreographyExecution(session, exec_id, path)

class ResetPasswordInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ResetPassword
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        super(ResetPasswordInputSet, self)._set_input('APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        super(ResetPasswordInputSet, self)._set_input('APIUser', value)
    def set_ConfirmPassword(self, value):
        """
        Set the value of the ConfirmPassword input for this Choreo. ((required, string) The new account password.  Must match the string entered in the Password variable.  Minumum password length is 6 characters.)
        """
        super(ResetPasswordInputSet, self)._set_input('ConfirmPassword', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) The new account password of 6 characters or more.)
        """
        super(ResetPasswordInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        super(ResetPasswordInputSet, self)._set_input('ResponseFormat', value)


class ResetPasswordResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ResetPassword Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class ResetPasswordChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ResetPasswordResultSet(response, path)
