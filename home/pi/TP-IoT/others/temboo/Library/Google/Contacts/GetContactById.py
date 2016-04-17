# -*- coding: utf-8 -*-

###############################################################################
#
# GetContactById
# Retrieves a specific contact with a given id.
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

class GetContactById(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetContactById Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetContactById, self).__init__(temboo_session, '/Library/Google/Contacts/GetContactById')


    def new_input_set(self):
        return GetContactByIdInputSet()

    def _make_result_set(self, result, path):
        return GetContactByIdResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetContactByIdChoreographyExecution(session, exec_id, path)

class GetContactByIdInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetContactById
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        super(GetContactByIdInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((required, string) The client ID provided by Google when you register your application.)
        """
        super(GetContactByIdInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((required, string) The client secret provided by Google when you registered your application.)
        """
        super(GetContactByIdInputSet, self)._set_input('ClientSecret', value)
    def set_ContactId(self, value):
        """
        Set the value of the ContactId input for this Choreo. ((required, string) The id associated with the contact to return. This can either be the individual id of the contact, or the full 'edit' link returned in the entry nodes of the GetAllContacts output.)
        """
        super(GetContactByIdInputSet, self)._set_input('ContactId', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used when an access token is expired or not provided.)
        """
        super(GetContactByIdInputSet, self)._set_input('RefreshToken', value)
    def set_UserEmail(self, value):
        """
        Set the value of the UserEmail input for this Choreo. ((required, string) The email address of the user whose contacts you want to retrieve. Defaults to "default," or the user whose OAuth access token is passed.)
        """
        super(GetContactByIdInputSet, self)._set_input('UserEmail', value)

class GetContactByIdResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetContactById Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_AccessToken(self):
        """
        Retrieve the value for the "AccessToken" output from this Choreo execution. ((optional, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        return self._output.get('AccessToken', None)

class GetContactByIdChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetContactByIdResultSet(response, path)
