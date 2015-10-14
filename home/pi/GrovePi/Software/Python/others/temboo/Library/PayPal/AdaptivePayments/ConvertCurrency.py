# -*- coding: utf-8 -*-

###############################################################################
#
# ConvertCurrency
# Converts a payment amount from one currency to another.
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

class ConvertCurrency(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ConvertCurrency Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ConvertCurrency, self).__init__(temboo_session, '/Library/PayPal/AdaptivePayments/ConvertCurrency')


    def new_input_set(self):
        return ConvertCurrencyInputSet()

    def _make_result_set(self, result, path):
        return ConvertCurrencyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ConvertCurrencyChoreographyExecution(session, exec_id, path)

class ConvertCurrencyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ConvertCurrency
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((required, decimal) The amount that should be converted to a new currency.)
        """
        super(ConvertCurrencyInputSet, self)._set_input('Amount', value)
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) Your PayPal AppID (or the default AppID for the PayPal sandbox).)
        """
        super(ConvertCurrencyInputSet, self)._set_input('AppID', value)
    def set_ConvertToCurrency(self, value):
        """
        Set the value of the ConvertToCurrency input for this Choreo. ((required, string) The currency code that you want to convert to (i.e. GBP).)
        """
        super(ConvertCurrencyInputSet, self)._set_input('ConvertToCurrency', value)
    def set_CurrencyCode(self, value):
        """
        Set the value of the CurrencyCode input for this Choreo. ((required, string) The currency code that you want to convert. (i.e. USD).)
        """
        super(ConvertCurrencyInputSet, self)._set_input('CurrencyCode', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The API Password provided by PayPal.)
        """
        super(ConvertCurrencyInputSet, self)._set_input('Password', value)
    def set_Signature(self, value):
        """
        Set the value of the Signature input for this Choreo. ((required, string) The API Signature provided by PayPal.)
        """
        super(ConvertCurrencyInputSet, self)._set_input('Signature', value)
    def set_UseSandbox(self, value):
        """
        Set the value of the UseSandbox input for this Choreo. ((conditional, boolean) Set to 1 to indicate that you're testing against the PayPal sandbox instead of production. Set to 0 (the default) when moving to production.)
        """
        super(ConvertCurrencyInputSet, self)._set_input('UseSandbox', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The API Username provided by PayPal.)
        """
        super(ConvertCurrencyInputSet, self)._set_input('Username', value)

class ConvertCurrencyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ConvertCurrency Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PayPal.)
        """
        return self._output.get('Response', None)

class ConvertCurrencyChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ConvertCurrencyResultSet(response, path)
