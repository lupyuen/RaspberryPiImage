# -*- coding: utf-8 -*-

###############################################################################
#
# CityStateLookup
# Lookup city and state using incomplete address information.
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

class CityStateLookup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CityStateLookup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CityStateLookup, self).__init__(temboo_session, '/Library/USPS/AddressInformationAPI/CityStateLookup')


    def new_input_set(self):
        return CityStateLookupInputSet()

    def _make_result_set(self, result, path):
        return CityStateLookupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CityStateLookupChoreographyExecution(session, exec_id, path)

class CityStateLookupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CityStateLookup
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) If you are accessing the production server, set to 'production'. Defaults to 'testing' which indicates that you are using the sandbox.)
        """
        super(CityStateLookupInputSet, self)._set_input('Endpoint', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password assigned by USPS)
        """
        super(CityStateLookupInputSet, self)._set_input('Password', value)
    def set_UserId(self, value):
        """
        Set the value of the UserId input for this Choreo. ((required, string) Alphanumeric ID assigned by USPS)
        """
        super(CityStateLookupInputSet, self)._set_input('UserId', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((required, integer) Maximum characters allowed: 5)
        """
        super(CityStateLookupInputSet, self)._set_input('Zip', value)

class CityStateLookupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CityStateLookup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from USPS Web Service)
        """
        return self._output.get('Response', None)

class CityStateLookupChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CityStateLookupResultSet(response, path)
