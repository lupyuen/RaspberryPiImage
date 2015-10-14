# -*- coding: utf-8 -*-

###############################################################################
#
# ServiceAvailability
# Retrieves available shipping options and delivery dates for a specified origin and destination.
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

class ServiceAvailability(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ServiceAvailability Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ServiceAvailability, self).__init__(temboo_session, '/Library/FedEx/Availability/ServiceAvailability')


    def new_input_set(self):
        return ServiceAvailabilityInputSet()

    def _make_result_set(self, result, path):
        return ServiceAvailabilityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ServiceAvailabilityChoreographyExecution(session, exec_id, path)

class ServiceAvailabilityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ServiceAvailability
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountNumber(self, value):
        """
        Set the value of the AccountNumber input for this Choreo. ((required, string) Your FedEx Account Number or Test Account Number.)
        """
        super(ServiceAvailabilityInputSet, self)._set_input('AccountNumber', value)
    def set_AuthenticationKey(self, value):
        """
        Set the value of the AuthenticationKey input for this Choreo. ((required, string) The Production Authentication Key or Development Test Key provided by FedEx Web Services.)
        """
        super(ServiceAvailabilityInputSet, self)._set_input('AuthenticationKey', value)
    def set_DestinationCountryCode(self, value):
        """
        Set the value of the DestinationCountryCode input for this Choreo. ((required, string) The destination country code to use for the service availability request (e.g., US).)
        """
        super(ServiceAvailabilityInputSet, self)._set_input('DestinationCountryCode', value)
    def set_DestinationPostalCode(self, value):
        """
        Set the value of the DestinationPostalCode input for this Choreo. ((required, string) The destination postal code to use for  the service availability request.)
        """
        super(ServiceAvailabilityInputSet, self)._set_input('DestinationPostalCode', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) Set to "test" to direct requests to the FedEx test environment. Defaults to "production" indicating that requests are sent to the production URL.)
        """
        super(ServiceAvailabilityInputSet, self)._set_input('Endpoint', value)
    def set_MeterNumber(self, value):
        """
        Set the value of the MeterNumber input for this Choreo. ((required, string) The Production or Test Meter Number provided by FedEx Web Services.)
        """
        super(ServiceAvailabilityInputSet, self)._set_input('MeterNumber', value)
    def set_OriginCountryCode(self, value):
        """
        Set the value of the OriginCountryCode input for this Choreo. ((required, string) The origin country code to use for the service availability request (e.g., US).)
        """
        super(ServiceAvailabilityInputSet, self)._set_input('OriginCountryCode', value)
    def set_OriginPostalCode(self, value):
        """
        Set the value of the OriginPostalCode input for this Choreo. ((required, string) The origin postal code to use for the service availability request.)
        """
        super(ServiceAvailabilityInputSet, self)._set_input('OriginPostalCode', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Production or Test Password provided by FedEx Web Services.)
        """
        super(ServiceAvailabilityInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(ServiceAvailabilityInputSet, self)._set_input('ResponseFormat', value)
    def set_ShipDate(self, value):
        """
        Set the value of the ShipDate input for this Choreo. ((optional, date) The date to use for the service availability request. Dates should be formatted as YYYY-MM-DD. Defautls to today's date.)
        """
        super(ServiceAvailabilityInputSet, self)._set_input('ShipDate', value)

class ServiceAvailabilityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ServiceAvailability Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from FedEx.)
        """
        return self._output.get('Response', None)

class ServiceAvailabilityChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ServiceAvailabilityResultSet(response, path)
