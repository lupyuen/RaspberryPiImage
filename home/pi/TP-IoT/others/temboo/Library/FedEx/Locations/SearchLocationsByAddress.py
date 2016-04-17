# -*- coding: utf-8 -*-

###############################################################################
#
# SearchLocationsByAddress
# Searches for FedEx locations near a given address.
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

class SearchLocationsByAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchLocationsByAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchLocationsByAddress, self).__init__(temboo_session, '/Library/FedEx/Locations/SearchLocationsByAddress')


    def new_input_set(self):
        return SearchLocationsByAddressInputSet()

    def _make_result_set(self, result, path):
        return SearchLocationsByAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchLocationsByAddressChoreographyExecution(session, exec_id, path)

class SearchLocationsByAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchLocationsByAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountNumber(self, value):
        """
        Set the value of the AccountNumber input for this Choreo. ((required, string) Your FedEx Account Number or Test Account Number.)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('AccountNumber', value)
    def set_AuthenticationKey(self, value):
        """
        Set the value of the AuthenticationKey input for this Choreo. ((required, string) The Production Authentication Key or Development Test Key provided by FedEx Web Services.)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('AuthenticationKey', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((required, string) The city associated with the location being searched.)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('City', value)
    def set_CountryCode(self, value):
        """
        Set the value of the CountryCode input for this Choreo. ((required, string) The country code associated with the location being searched (e.g., US).)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('CountryCode', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) Set to "test" to direct requests to the FedEx test environment. Defaults to "production" indicating that requests are sent to the production URL.)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('Endpoint', value)
    def set_MeterNumber(self, value):
        """
        Set the value of the MeterNumber input for this Choreo. ((required, string) The Production or Test Meter Number provided by FedEx Web Services.)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('MeterNumber', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Production or Test Password provided by FedEx Web Services.)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('Password', value)
    def set_PostalCode(self, value):
        """
        Set the value of the PostalCode input for this Choreo. ((required, string) The postal code associated with the location being searched.)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('PostalCode', value)
    def set_RadiusDistance(self, value):
        """
        Set the value of the RadiusDistance input for this Choreo. ((optional, decimal) Specifies value of the radius around the address to search for FedEx locations. Note that RadiusUnits applies to this value. Defaults to 10 miles.)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('RadiusDistance', value)
    def set_RadiusUnits(self, value):
        """
        Set the value of the RadiusUnits input for this Choreo. ((optional, string) Specifies the unit of measure for the RadiusDistance value. Valid values are mi (the default) and km.)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('RadiusUnits', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('ResponseFormat', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) Specifies the criterion to be used to sort the location details. Valid values are: distance (the default), latest_express_dropoff_time, latest_ground_dropoff_time, location_type.)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('SortBy', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Specifies sort order of the location details. Valid values are: lowest_to_highest (the default) and highest_to_lowest.)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('SortOrder', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((required, string) Identifying abbreviation for US state, Canada province (e.g., NY).)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('State', value)
    def set_Street(self, value):
        """
        Set the value of the Street input for this Choreo. ((required, string) The street number and street name (e.g., 350 5th Ave).)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('Street', value)
    def set_SupportedServices(self, value):
        """
        Set the value of the SupportedServices input for this Choreo. ((optional, string) Specifies the types of services supported by a FedEx location for redirect to hold. Valid values are: fedex_express, fedex_ground, fedex_ground_home_delivery.)
        """
        super(SearchLocationsByAddressInputSet, self)._set_input('SupportedServices', value)

class SearchLocationsByAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchLocationsByAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from FedEx.)
        """
        return self._output.get('Response', None)

class SearchLocationsByAddressChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchLocationsByAddressResultSet(response, path)
