# -*- coding: utf-8 -*-

###############################################################################
#
# CreateContact
# Creates a contact in your Constant Contact account.
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

class CreateContact(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateContact Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateContact, self).__init__(temboo_session, '/Library/ConstantContact/CreateContact')


    def new_input_set(self):
        return CreateContactInputSet()

    def _make_result_set(self, result, path):
        return CreateContactResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateContactChoreographyExecution(session, exec_id, path)

class CreateContactInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateContact
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Constant Contact.)
        """
        super(CreateContactInputSet, self)._set_input('APIKey', value)
    def set_Addr1(self, value):
        """
        Set the value of the Addr1 input for this Choreo. ((optional, string) The first line of the contact's address.)
        """
        super(CreateContactInputSet, self)._set_input('Addr1', value)
    def set_Addr2(self, value):
        """
        Set the value of the Addr2 input for this Choreo. ((optional, string) The second line of the contact's address.)
        """
        super(CreateContactInputSet, self)._set_input('Addr2', value)
    def set_Addr3(self, value):
        """
        Set the value of the Addr3 input for this Choreo. ((optional, string) The third line of the contact's address.)
        """
        super(CreateContactInputSet, self)._set_input('Addr3', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) The city portion of the contact's address.)
        """
        super(CreateContactInputSet, self)._set_input('City', value)
    def set_CompanyName(self, value):
        """
        Set the value of the CompanyName input for this Choreo. ((optional, string) The company name for the contact.)
        """
        super(CreateContactInputSet, self)._set_input('CompanyName', value)
    def set_CountryCode(self, value):
        """
        Set the value of the CountryCode input for this Choreo. ((optional, string) The country code associated with the contact's address.)
        """
        super(CreateContactInputSet, self)._set_input('CountryCode', value)
    def set_CountryName(self, value):
        """
        Set the value of the CountryName input for this Choreo. ((optional, string) Corresponds to the Country Name field in Constant Contact)
        """
        super(CreateContactInputSet, self)._set_input('CountryName', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((required, string) The email address for the contact.)
        """
        super(CreateContactInputSet, self)._set_input('EmailAddress', value)
    def set_EmailType(self, value):
        """
        Set the value of the EmailType input for this Choreo. ((optional, string) The email type that the contact should receive.)
        """
        super(CreateContactInputSet, self)._set_input('EmailType', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((optional, string) The first name of the contact.)
        """
        super(CreateContactInputSet, self)._set_input('FirstName', value)
    def set_HomePhone(self, value):
        """
        Set the value of the HomePhone input for this Choreo. ((optional, string) The contact's home phone.)
        """
        super(CreateContactInputSet, self)._set_input('HomePhone', value)
    def set_JobTitle(self, value):
        """
        Set the value of the JobTitle input for this Choreo. ((optional, string) The contact's job title.)
        """
        super(CreateContactInputSet, self)._set_input('JobTitle', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((optional, string) The last name of the contact.)
        """
        super(CreateContactInputSet, self)._set_input('LastName', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, integer) The ID for the list that you want to add the contact to.)
        """
        super(CreateContactInputSet, self)._set_input('ListId', value)
    def set_MiddleName(self, value):
        """
        Set the value of the MiddleName input for this Choreo. ((optional, string) The middle name of the contact.)
        """
        super(CreateContactInputSet, self)._set_input('MiddleName', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((optional, string) The full name of the contact.)
        """
        super(CreateContactInputSet, self)._set_input('Name', value)
    def set_Note(self, value):
        """
        Set the value of the Note input for this Choreo. ((optional, string) A note associated with the contact.)
        """
        super(CreateContactInputSet, self)._set_input('Note', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Constant Contact password.)
        """
        super(CreateContactInputSet, self)._set_input('Password', value)
    def set_PostalCode(self, value):
        """
        Set the value of the PostalCode input for this Choreo. ((optional, string) The postal code for the contact's address.)
        """
        super(CreateContactInputSet, self)._set_input('PostalCode', value)
    def set_StateCode(self, value):
        """
        Set the value of the StateCode input for this Choreo. ((optional, string) The state code for the contact's address.)
        """
        super(CreateContactInputSet, self)._set_input('StateCode', value)
    def set_StateName(self, value):
        """
        Set the value of the StateName input for this Choreo. ((optional, string) Corresponds to the State Name field in Constant Contact)
        """
        super(CreateContactInputSet, self)._set_input('StateName', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((optional, string) The status of the contact (i.e. Active).)
        """
        super(CreateContactInputSet, self)._set_input('Status', value)
    def set_SubPostalCode(self, value):
        """
        Set the value of the SubPostalCode input for this Choreo. ((optional, string) The sub postal code for the contact.)
        """
        super(CreateContactInputSet, self)._set_input('SubPostalCode', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) Your Constant Contact username.)
        """
        super(CreateContactInputSet, self)._set_input('UserName', value)
    def set_WorkPhone(self, value):
        """
        Set the value of the WorkPhone input for this Choreo. ((optional, string) The contact's work phone.)
        """
        super(CreateContactInputSet, self)._set_input('WorkPhone', value)

class CreateContactResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateContact Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Constant Contact.)
        """
        return self._output.get('Response', None)

class CreateContactChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateContactResultSet(response, path)
