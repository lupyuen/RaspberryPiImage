# -*- coding: utf-8 -*-

###############################################################################
#
# TrackByNumber
# Retrieves shipment information for a specified tracking number.
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

class TrackByNumber(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TrackByNumber Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TrackByNumber, self).__init__(temboo_session, '/Library/FedEx/TrackingAndVisibility/TrackByNumber')


    def new_input_set(self):
        return TrackByNumberInputSet()

    def _make_result_set(self, result, path):
        return TrackByNumberResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TrackByNumberChoreographyExecution(session, exec_id, path)

class TrackByNumberInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TrackByNumber
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountNumber(self, value):
        """
        Set the value of the AccountNumber input for this Choreo. ((required, string) Your FedEx Account Number or Test Account Number.)
        """
        super(TrackByNumberInputSet, self)._set_input('AccountNumber', value)
    def set_AuthenticationKey(self, value):
        """
        Set the value of the AuthenticationKey input for this Choreo. ((required, string) The Production Authentication Key or Development Test Key provided by FedEx Web Services.)
        """
        super(TrackByNumberInputSet, self)._set_input('AuthenticationKey', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) Set to "test" to direct requests to the FedEx test environment. Defaults to "production" indicating that requests are sent to the production URL.)
        """
        super(TrackByNumberInputSet, self)._set_input('Endpoint', value)
    def set_MeterNumber(self, value):
        """
        Set the value of the MeterNumber input for this Choreo. ((required, string) The Production or Test Meter Number provided by FedEx Web Services.)
        """
        super(TrackByNumberInputSet, self)._set_input('MeterNumber', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Production or Test Password provided by FedEx Web Services.)
        """
        super(TrackByNumberInputSet, self)._set_input('Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(TrackByNumberInputSet, self)._set_input('ResponseFormat', value)
    def set_TrackingNumber(self, value):
        """
        Set the value of the TrackingNumber input for this Choreo. ((required, string) The tracking number for the shipment.)
        """
        super(TrackByNumberInputSet, self)._set_input('TrackingNumber', value)

class TrackByNumberResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TrackByNumber Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from FedEx.)
        """
        return self._output.get('Response', None)

class TrackByNumberChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TrackByNumberResultSet(response, path)
