# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateUserIdentity
# Updates the User Identity.    This API method only allows you to set an identity as verified.
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

class UpdateUserIdentity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateUserIdentity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateUserIdentity, self).__init__(temboo_session, '/Library/Zendesk/UserIdentities/UpdateUserIdentity')


    def new_input_set(self):
        return UpdateUserIdentityInputSet()

    def _make_result_set(self, result, path):
        return UpdateUserIdentityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateUserIdentityChoreographyExecution(session, exec_id, path)

class UpdateUserIdentityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateUserIdentity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        super(UpdateUserIdentityInputSet, self)._set_input('Email', value)
    def set_IdentityID(self, value):
        """
        Set the value of the IdentityID input for this Choreo. ((conditional, string) The ID of the Identity to be updated.)
        """
        super(UpdateUserIdentityInputSet, self)._set_input('IdentityID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        super(UpdateUserIdentityInputSet, self)._set_input('Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        super(UpdateUserIdentityInputSet, self)._set_input('Server', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((conditional, string) The ID of the user.)
        """
        super(UpdateUserIdentityInputSet, self)._set_input('UserID', value)
    def set_Verified(self, value):
        """
        Set the value of the Verified input for this Choreo. ((required, string) Specifies whether the identity has been verified (true or false).)
        """
        super(UpdateUserIdentityInputSet, self)._set_input('Verified', value)

class UpdateUserIdentityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateUserIdentity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class UpdateUserIdentityChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateUserIdentityResultSet(response, path)
