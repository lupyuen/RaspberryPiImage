# -*- coding: utf-8 -*-

###############################################################################
#
# FindByAddress
# Retrieves complete geocoding information for a location by specifying an address or partial address.
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

class FindByAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindByAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FindByAddress, self).__init__(temboo_session, '/Library/Yahoo/PlaceFinder/FindByAddress')


    def new_input_set(self):
        return FindByAddressInputSet()

    def _make_result_set(self, result, path):
        return FindByAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindByAddressChoreographyExecution(session, exec_id, path)

class FindByAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindByAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((required, string) The address to be searched.)
        """
        super(FindByAddressInputSet, self)._set_input('Address', value)
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(FindByAddressInputSet, self)._set_input('AppID', value)
    def set_GeocodeFlags(self, value):
        """
        Set the value of the GeocodeFlags input for this Choreo. ((optional, string) Affects how geocoding is performed for the request. Valid value are: A, C, L, Q, or R. See documentation for more details on this parameter.)
        """
        super(FindByAddressInputSet, self)._set_input('GeocodeFlags', value)
    def set_ResponseFlags(self, value):
        """
        Set the value of the ResponseFlags input for this Choreo. ((optional, string) Determines which data elements are returned in the response. Valid values are: B, C, D, E, G, I, J, Q, R, T, U, W, X. See documentation for details on this parameter.)
        """
        super(FindByAddressInputSet, self)._set_input('ResponseFlags', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(FindByAddressInputSet, self)._set_input('ResponseFormat', value)

class FindByAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindByAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Yahoo PlaceFinder.)
        """
        return self._output.get('Response', None)
    def get_Latitude(self):
        """
        Retrieve the value for the "Latitude" output from this Choreo execution. ((decimal) The latitude coordinate for the location.)
        """
        return self._output.get('Latitude', None)
    def get_Longitude(self):
        """
        Retrieve the value for the "Longitude" output from this Choreo execution. ((decimal) The longitude coordinate for the location.)
        """
        return self._output.get('Longitude', None)
    def get_WOEID(self):
        """
        Retrieve the value for the "WOEID" output from this Choreo execution. ((integer) The unique Where On Earth ID of the location.)
        """
        return self._output.get('WOEID', None)

class FindByAddressChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FindByAddressResultSet(response, path)
