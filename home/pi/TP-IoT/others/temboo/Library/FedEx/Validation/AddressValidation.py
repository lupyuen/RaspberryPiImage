# -*- coding: utf-8 -*-

###############################################################################
#
# AddressValidation
# Validates a given address.
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

class AddressValidation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddressValidation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddressValidation, self).__init__(temboo_session, '/Library/FedEx/Validation/AddressValidation')


    def new_input_set(self):
        return AddressValidationInputSet()

    def _make_result_set(self, result, path):
        return AddressValidationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddressValidationChoreographyExecution(session, exec_id, path)

class AddressValidationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddressValidation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountNumber(self, value):
        """
        Set the value of the AccountNumber input for this Choreo. ((required, string) Your FedEx Account Number or Test Account Number.)
        """
        super(AddressValidationInputSet, self)._set_input('AccountNumber', value)
    def set_AuthenticationKey(self, value):
        """
        Set the value of the AuthenticationKey input for this Choreo. ((required, string) The Production Authentication Key or Development Test Key provided by FedEx Web Services.)
        """
        super(AddressValidationInputSet, self)._set_input('AuthenticationKey', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((conditional, string) The name of the city or town.)
        """
        super(AddressValidationInputSet, self)._set_input('City', value)
    def set_ClientReferenceID(self, value):
        """
        Set the value of the ClientReferenceID input for this Choreo. ((optional, string) A reference id provided by the client.)
        """
        super(AddressValidationInputSet, self)._set_input('ClientReferenceID', value)
    def set_CompanyName(self, value):
        """
        Set the value of the CompanyName input for this Choreo. ((optional, string) Identifies the company associated with the location.)
        """
        super(AddressValidationInputSet, self)._set_input('CompanyName', value)
    def set_CountryCode(self, value):
        """
        Set the value of the CountryCode input for this Choreo. ((conditional, string) The country code associated with the address being validated (e.g., US).)
        """
        super(AddressValidationInputSet, self)._set_input('CountryCode', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) Set to "test" to direct requests to the FedEx test environment. Defaults to "production" indicating that requests are sent to the production URL.)
        """
        super(AddressValidationInputSet, self)._set_input('Endpoint', value)
    def set_MeterNumber(self, value):
        """
        Set the value of the MeterNumber input for this Choreo. ((required, string) The Production or Test Meter Number provided by FedEx Web Services.)
        """
        super(AddressValidationInputSet, self)._set_input('MeterNumber', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Production or Test Password provided by FedEx Web Services.)
        """
        super(AddressValidationInputSet, self)._set_input('Password', value)
    def set_PhoneNumber(self, value):
        """
        Set the value of the PhoneNumber input for this Choreo. ((optional, string) Identifies the phone number associated with the contact being validated.)
        """
        super(AddressValidationInputSet, self)._set_input('PhoneNumber', value)
    def set_PostalCode(self, value):
        """
        Set the value of the PostalCode input for this Choreo. ((conditional, string) The postal code associated with the address being validated.)
        """
        super(AddressValidationInputSet, self)._set_input('PostalCode', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(AddressValidationInputSet, self)._set_input('ResponseFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((conditional, string) Identifying abbreviation for US state, Canada province (e.g., NY).)
        """
        super(AddressValidationInputSet, self)._set_input('State', value)
    def set_Street(self, value):
        """
        Set the value of the Street input for this Choreo. ((conditional, string) The street number and street name (e.g., 350 5th Ave).)
        """
        super(AddressValidationInputSet, self)._set_input('Street', value)
    def set_UrbanizationCode(self, value):
        """
        Set the value of the UrbanizationCode input for this Choreo. ((optional, string) Relevant only to addresses in Puerto Rico.)
        """
        super(AddressValidationInputSet, self)._set_input('UrbanizationCode', value)

class AddressValidationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddressValidation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from FedEx.)
        """
        return self._output.get('Response', None)

class AddressValidationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddressValidationResultSet(response, path)
