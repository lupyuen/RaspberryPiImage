# -*- coding: utf-8 -*-

###############################################################################
#
# ExecutePayment
# Executes a PayPal payment that has been accepted and approved.
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

class ExecutePayment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ExecutePayment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ExecutePayment, self).__init__(temboo_session, '/Library/PayPal/Payments/ExecutePayment')


    def new_input_set(self):
        return ExecutePaymentInputSet()

    def _make_result_set(self, result, path):
        return ExecutePaymentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ExecutePaymentChoreographyExecution(session, exec_id, path)

class ExecutePaymentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ExecutePayment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_PayerID(self, value):
        """
        Set the value of the PayerID input for this Choreo. ((required, string) The id of the user who is making a payment.)
        """
        super(ExecutePaymentInputSet, self)._set_input('PayerID', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved from PayPal. Required unless providing the ClientID and ClientSecret which can be used to generate a new access token.)
        """
        super(ExecutePaymentInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by PayPal. Required unless a valid Access Token is provided.)
        """
        super(ExecutePaymentInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by PayPal. Required unless a valid Access Token is provided.)
        """
        super(ExecutePaymentInputSet, self)._set_input('ClientSecret', value)
    def set_PaymentID(self, value):
        """
        Set the value of the PaymentID input for this Choreo. ((required, string) The id of the payment to execute.)
        """
        super(ExecutePaymentInputSet, self)._set_input('PaymentID', value)
    def set_Scope(self, value):
        """
        Set the value of the Scope input for this Choreo. ((optional, string) A space delimited list of resource URL endpoints that the token should have access for. This is only used when providing the ClientID and Client Secret in order to generate a new access token.)
        """
        super(ExecutePaymentInputSet, self)._set_input('Scope', value)
    def set_UseSandbox(self, value):
        """
        Set the value of the UseSandbox input for this Choreo. ((conditional, boolean) Set to 1 to indicate that you're testing against the PayPal sandbox instead of production. Set to 0 (the default) when moving to production.)
        """
        super(ExecutePaymentInputSet, self)._set_input('UseSandbox', value)

class ExecutePaymentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ExecutePayment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PayPal.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) The new access token retrieved from PayPal when providing the Client ID and Client Secret.)
        """
        return self._output.get('NewAccessToken', None)
    def get_SaleID(self):
        """
        Retrieve the value for the "SaleID" output from this Choreo execution. ((string) The id of the sale that was just executed. This can be used to Lookup the sales transaction if needed.)
        """
        return self._output.get('SaleID', None)

class ExecutePaymentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ExecutePaymentResultSet(response, path)
