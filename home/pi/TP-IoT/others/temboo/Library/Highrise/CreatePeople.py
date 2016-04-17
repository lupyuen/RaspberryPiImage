# -*- coding: utf-8 -*-

###############################################################################
#
# CreatePeople
# Creates a new contact record in your Highrise CRM.
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

class CreatePeople(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreatePeople Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreatePeople, self).__init__(temboo_session, '/Library/Highrise/CreatePeople')


    def new_input_set(self):
        return CreatePeopleInputSet()

    def _make_result_set(self, result, path):
        return CreatePeopleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreatePeopleChoreographyExecution(session, exec_id, path)

class CreatePeopleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreatePeople
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Highrise account name. This is the first part of the account's URL.)
        """
        super(CreatePeopleInputSet, self)._set_input('AccountName', value)
    def set_Background(self, value):
        """
        Set the value of the Background input for this Choreo. ((optional, string) Corresponds to the background field in Highrise)
        """
        super(CreatePeopleInputSet, self)._set_input('Background', value)
    def set_CompanyName(self, value):
        """
        Set the value of the CompanyName input for this Choreo. ((optional, string) Corresponds to the company name field in Highrise.)
        """
        super(CreatePeopleInputSet, self)._set_input('CompanyName', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((optional, string) Corresponds to the email address field in Highrise.)
        """
        super(CreatePeopleInputSet, self)._set_input('EmailAddress', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((required, string) Corresponds to the first name field in Highrise.)
        """
        super(CreatePeopleInputSet, self)._set_input('FirstName', value)
    def set_HomePhone(self, value):
        """
        Set the value of the HomePhone input for this Choreo. ((optional, string) Corresponds to the home phone field in Highrise.)
        """
        super(CreatePeopleInputSet, self)._set_input('HomePhone', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((optional, string) Corresponds to the last name field in Highrise.)
        """
        super(CreatePeopleInputSet, self)._set_input('LastName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Highrise account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        super(CreatePeopleInputSet, self)._set_input('Password', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) Corresponds to the title field in Highrise.)
        """
        super(CreatePeopleInputSet, self)._set_input('Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Highrise account username or API Key.)
        """
        super(CreatePeopleInputSet, self)._set_input('Username', value)
    def set_WorkPhone(self, value):
        """
        Set the value of the WorkPhone input for this Choreo. ((optional, string) Corresponds to the work phone field in Highrise.)
        """
        super(CreatePeopleInputSet, self)._set_input('WorkPhone', value)

class CreatePeopleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreatePeople Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Highrise.)
        """
        return self._output.get('Response', None)

class CreatePeopleChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreatePeopleResultSet(response, path)
