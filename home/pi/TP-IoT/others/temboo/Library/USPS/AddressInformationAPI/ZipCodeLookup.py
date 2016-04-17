# -*- coding: utf-8 -*-

###############################################################################
#
# ZipCodeLookup
# Lookup zip codes using incomplete address information.
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

class ZipCodeLookup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ZipCodeLookup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ZipCodeLookup, self).__init__(temboo_session, '/Library/USPS/AddressInformationAPI/ZipCodeLookup')


    def new_input_set(self):
        return ZipCodeLookupInputSet()

    def _make_result_set(self, result, path):
        return ZipCodeLookupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ZipCodeLookupChoreographyExecution(session, exec_id, path)

class ZipCodeLookupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ZipCodeLookup
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AptOrSuite(self, value):
        """
        Set the value of the AptOrSuite input for this Choreo. ((optional, string) Used to provide an apartment or suite number, if applicable. Maximum characters allowed: 38.)
        """
        super(ZipCodeLookupInputSet, self)._set_input('AptOrSuite', value)
    def set_ApyOrSuite(self, value):
        """
        Set the value of the ApyOrSuite input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(ZipCodeLookupInputSet, self)._set_input('ApyOrSuite', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((required, string) Maximum characters allowed: 15.)
        """
        super(ZipCodeLookupInputSet, self)._set_input('City', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) If you are accessing the production server, set to 'production'. Defaults to 'testing' which indicates that you are using the sandbox.)
        """
        super(ZipCodeLookupInputSet, self)._set_input('Endpoint', value)
    def set_FirmName(self, value):
        """
        Set the value of the FirmName input for this Choreo. ((optional, string) Maximum characters allowed: 38.)
        """
        super(ZipCodeLookupInputSet, self)._set_input('FirmName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password assigned by USPS)
        """
        super(ZipCodeLookupInputSet, self)._set_input('Password', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((required, string) Maximum characters allowed: 2.)
        """
        super(ZipCodeLookupInputSet, self)._set_input('State', value)
    def set_StreetAddress(self, value):
        """
        Set the value of the StreetAddress input for this Choreo. ((required, string) Street address.  Maximum characters allowed: 38.)
        """
        super(ZipCodeLookupInputSet, self)._set_input('StreetAddress', value)
    def set_UserId(self, value):
        """
        Set the value of the UserId input for this Choreo. ((required, string) Alphanumeric ID assigned by USPS)
        """
        super(ZipCodeLookupInputSet, self)._set_input('UserId', value)

class ZipCodeLookupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ZipCodeLookup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from USPS Web Service)
        """
        return self._output.get('Response', None)

class ZipCodeLookupChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ZipCodeLookupResultSet(response, path)
