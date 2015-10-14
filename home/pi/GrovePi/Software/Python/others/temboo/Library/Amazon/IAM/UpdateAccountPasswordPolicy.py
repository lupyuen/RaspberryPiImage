# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateAccountPasswordPolicy
# Updates the password policy settings for the account.
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

class UpdateAccountPasswordPolicy(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateAccountPasswordPolicy Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateAccountPasswordPolicy, self).__init__(temboo_session, '/Library/Amazon/IAM/UpdateAccountPasswordPolicy')


    def new_input_set(self):
        return UpdateAccountPasswordPolicyInputSet()

    def _make_result_set(self, result, path):
        return UpdateAccountPasswordPolicyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateAccountPasswordPolicyChoreographyExecution(session, exec_id, path)

class UpdateAccountPasswordPolicyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateAccountPasswordPolicy
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(UpdateAccountPasswordPolicyInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(UpdateAccountPasswordPolicyInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_AllowUsersToChangePassword(self, value):
        """
        Set the value of the AllowUsersToChangePassword input for this Choreo. ((optional, boolean) Determines whether users can set/change their own passwords. Valid values: "true" or "false" (the default).)
        """
        super(UpdateAccountPasswordPolicyInputSet, self)._set_input('AllowUsersToChangePassword', value)
    def set_ExpirePasswords(self, value):
        """
        Set the value of the ExpirePasswords input for this Choreo. ((optional, boolean) Determines whether the passwords expire. Valid values: "true" or "false" (the default).)
        """
        super(UpdateAccountPasswordPolicyInputSet, self)._set_input('ExpirePasswords', value)
    def set_MaxPasswordsAge(self, value):
        """
        Set the value of the MaxPasswordsAge input for this Choreo. ((optional, integer) Maximum age of the passwords before they expire.)
        """
        super(UpdateAccountPasswordPolicyInputSet, self)._set_input('MaxPasswordsAge', value)
    def set_MinimumPasswordLength(self, value):
        """
        Set the value of the MinimumPasswordLength input for this Choreo. ((optional, integer) Mininum length of the password. Defaults to none.)
        """
        super(UpdateAccountPasswordPolicyInputSet, self)._set_input('MinimumPasswordLength', value)
    def set_RequireLowercaseCharacters(self, value):
        """
        Set the value of the RequireLowercaseCharacters input for this Choreo. ((optional, boolean) Determines whether at least one lower-case character is required in the password. Valid values: "true" or "false" (the default).)
        """
        super(UpdateAccountPasswordPolicyInputSet, self)._set_input('RequireLowercaseCharacters', value)
    def set_RequireNumbers(self, value):
        """
        Set the value of the RequireNumbers input for this Choreo. ((optional, boolean) Determines whether numbers are required in the password. Valid values: "true" or "false" (the default).)
        """
        super(UpdateAccountPasswordPolicyInputSet, self)._set_input('RequireNumbers', value)
    def set_RequireSymbols(self, value):
        """
        Set the value of the RequireSymbols input for this Choreo. ((optional, boolean) Determines whether symbols are required in the password. Valid values: "true" or "false" (the default).)
        """
        super(UpdateAccountPasswordPolicyInputSet, self)._set_input('RequireSymbols', value)
    def set_RequireUppercaseCharacters(self, value):
        """
        Set the value of the RequireUppercaseCharacters input for this Choreo. ((optional, boolean) Determines whether at least one upper-case character is required in the password. Valid values: "true" or "false" (the default).)
        """
        super(UpdateAccountPasswordPolicyInputSet, self)._set_input('RequireUppercaseCharacters', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(UpdateAccountPasswordPolicyInputSet, self)._set_input('ResponseFormat', value)

class UpdateAccountPasswordPolicyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateAccountPasswordPolicy Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class UpdateAccountPasswordPolicyChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateAccountPasswordPolicyResultSet(response, path)
