# -*- coding: utf-8 -*-

###############################################################################
#
# TrackByReference
# Retrieves shipment information for a specified reference number.
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

class TrackByReference(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TrackByReference Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TrackByReference, self).__init__(temboo_session, '/Library/FedEx/TrackingAndVisibility/TrackByReference')


    def new_input_set(self):
        return TrackByReferenceInputSet()

    def _make_result_set(self, result, path):
        return TrackByReferenceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TrackByReferenceChoreographyExecution(session, exec_id, path)

class TrackByReferenceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TrackByReference
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountNumber(self, value):
        """
        Set the value of the AccountNumber input for this Choreo. ((required, string) Your FedEx Account Number or Test Account Number.)
        """
        super(TrackByReferenceInputSet, self)._set_input('AccountNumber', value)
    def set_AuthenticationKey(self, value):
        """
        Set the value of the AuthenticationKey input for this Choreo. ((required, string) The Production Authentication Key or Development Test Key provided by FedEx Web Services.)
        """
        super(TrackByReferenceInputSet, self)._set_input('AuthenticationKey', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) The destination city.)
        """
        super(TrackByReferenceInputSet, self)._set_input('City', value)
    def set_CountryCode(self, value):
        """
        Set the value of the CountryCode input for this Choreo. ((conditional, string) The country code associated with the shipment destination (e.g., US). Required unless specifying the ShipmentAccountNumber.)
        """
        super(TrackByReferenceInputSet, self)._set_input('CountryCode', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) Set to "test" to direct requests to the FedEx test environment. Defaults to "production" indicating that requests are sent to the production URL.)
        """
        super(TrackByReferenceInputSet, self)._set_input('Endpoint', value)
    def set_MeterNumber(self, value):
        """
        Set the value of the MeterNumber input for this Choreo. ((required, string) The Production or Test Meter Number provided by FedEx Web Services.)
        """
        super(TrackByReferenceInputSet, self)._set_input('MeterNumber', value)
    def set_OperatingCompany(self, value):
        """
        Set the value of the OperatingCompany input for this Choreo. ((required, string) Identification for a fedex operating company (e.g.,  fedex_express, fedex_freight, fedex_ground). See Choreo notes for allowed values.)
        """
        super(TrackByReferenceInputSet, self)._set_input('OperatingCompany', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Production or Test Password provided by FedEx Web Services.)
        """
        super(TrackByReferenceInputSet, self)._set_input('Password', value)
    def set_PostalCode(self, value):
        """
        Set the value of the PostalCode input for this Choreo. ((conditional, string) The postal code associated with the shipment destination. Required unless specifying the ShipmentAccountNumber.)
        """
        super(TrackByReferenceInputSet, self)._set_input('PostalCode', value)
    def set_Reference(self, value):
        """
        Set the value of the Reference input for this Choreo. ((required, string) A reference number for tracking the shipment.)
        """
        super(TrackByReferenceInputSet, self)._set_input('Reference', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(TrackByReferenceInputSet, self)._set_input('ResponseFormat', value)
    def set_ShipDateRangeBegin(self, value):
        """
        Set the value of the ShipDateRangeBegin input for this Choreo. ((optional, date) Specifies the beginning of a date range used to narrow the search to a period in time. Dates should be formatted as YYYY-MM-DD.)
        """
        super(TrackByReferenceInputSet, self)._set_input('ShipDateRangeBegin', value)
    def set_ShipDateRangeEnd(self, value):
        """
        Set the value of the ShipDateRangeEnd input for this Choreo. ((optional, date) Specifies the beginning of a date range used to narrow the search to a period in time. Dates should be formatted as YYYY-MM-DD.)
        """
        super(TrackByReferenceInputSet, self)._set_input('ShipDateRangeEnd', value)
    def set_ShipmentAccountNumber(self, value):
        """
        Set the value of the ShipmentAccountNumber input for this Choreo. ((conditional, string) The shipment account number. Required unless specifying the PostalCode and CountryCode.)
        """
        super(TrackByReferenceInputSet, self)._set_input('ShipmentAccountNumber', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) Identifying abbreviation for US state, Canada province of the shipment destination (e.g., NY).)
        """
        super(TrackByReferenceInputSet, self)._set_input('State', value)
    def set_Street(self, value):
        """
        Set the value of the Street input for this Choreo. ((optional, string) The street number and street name for the shipment destination (e.g., 350 5th Ave).)
        """
        super(TrackByReferenceInputSet, self)._set_input('Street', value)

class TrackByReferenceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TrackByReference Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from FedEx.)
        """
        return self._output.get('Response', None)

class TrackByReferenceChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TrackByReferenceResultSet(response, path)
