# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateContact
# Update an existing contact's information.
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

class UpdateContact(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateContact Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateContact, self).__init__(temboo_session, '/Library/Google/Contacts/UpdateContact')


    def new_input_set(self):
        return UpdateContactInputSet()

    def _make_result_set(self, result, path):
        return UpdateContactResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateContactChoreographyExecution(session, exec_id, path)

class UpdateContactInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateContact
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        super(UpdateContactInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The OAuth client ID provided by Google when you register your application.)
        """
        super(UpdateContactInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The OAuth client secret provided by Google when you registered your application.)
        """
        super(UpdateContactInputSet, self)._set_input('ClientSecret', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((conditional, string) The id of the contact to update. Required unless providing a value for the Query input.)
        """
        super(UpdateContactInputSet, self)._set_input('ID', value)
    def set_NewEmail(self, value):
        """
        Set the value of the NewEmail input for this Choreo. ((conditional, string) The contact's new email address.)
        """
        super(UpdateContactInputSet, self)._set_input('NewEmail', value)
    def set_NewFirstName(self, value):
        """
        Set the value of the NewFirstName input for this Choreo. ((conditional, string) The contact's new first name.)
        """
        super(UpdateContactInputSet, self)._set_input('NewFirstName', value)
    def set_NewLastName(self, value):
        """
        Set the value of the NewLastName input for this Choreo. ((conditional, string) The contact's new last name.)
        """
        super(UpdateContactInputSet, self)._set_input('NewLastName', value)
    def set_NewPhone(self, value):
        """
        Set the value of the NewPhone input for this Choreo. ((optional, string) The contact's new telephone number.)
        """
        super(UpdateContactInputSet, self)._set_input('NewPhone', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((conditional, string) A search term to retrieve the contact to update, such as an email address, last name, or address. Required unless providing a value for the ID input.)
        """
        super(UpdateContactInputSet, self)._set_input('Query', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) The refresh token retrieved in the last step of the OAuth process. This is used when an access token is expired or not provided.)
        """
        super(UpdateContactInputSet, self)._set_input('RefreshToken', value)

class UpdateContactResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateContact Choreo.
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
    def get_ContactID(self):
        """
        Retrieve the value for the "ContactID" output from this Choreo execution. ((string) The unique ID for the contact returned by Google.)
        """
        return self._output.get('ContactID', None)
    def get_Email(self):
        """
        Retrieve the value for the "Email" output from this Choreo execution. ((string) The contact's current email address.)
        """
        return self._output.get('Email', None)
    def get_FirstName(self):
        """
        Retrieve the value for the "FirstName" output from this Choreo execution. ((string) The contact's current given name.)
        """
        return self._output.get('FirstName', None)
    def get_LastName(self):
        """
        Retrieve the value for the "LastName" output from this Choreo execution. ((string) The contact's current family name.)
        """
        return self._output.get('LastName', None)
    def get_Phone(self):
        """
        Retrieve the value for the "Phone" output from this Choreo execution. ((string) The contact's current telephone number.)
        """
        return self._output.get('Phone', None)

class UpdateContactChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateContactResultSet(response, path)
