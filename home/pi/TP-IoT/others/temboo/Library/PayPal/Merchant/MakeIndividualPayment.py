# -*- coding: utf-8 -*-

###############################################################################
#
# MakeIndividualPayment
# Retrieves the available balance for a PayPal account.
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

class MakeIndividualPayment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MakeIndividualPayment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(MakeIndividualPayment, self).__init__(temboo_session, '/Library/PayPal/Merchant/MakeIndividualPayment')


    def new_input_set(self):
        return MakeIndividualPaymentInputSet()

    def _make_result_set(self, result, path):
        return MakeIndividualPaymentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MakeIndividualPaymentChoreographyExecution(session, exec_id, path)

class MakeIndividualPaymentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MakeIndividualPayment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CurrencyCode(self, value):
        """
        Set the value of the CurrencyCode input for this Choreo. ((optional, string) The currency code associated with the PaymentAmount. Defaults to "USD".)
        """
        super(MakeIndividualPaymentInputSet, self)._set_input('CurrencyCode', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((required, string) The email address used to identify the recipient of the payment.)
        """
        super(MakeIndividualPaymentInputSet, self)._set_input('EmailAddress', value)
    def set_EmailSubject(self, value):
        """
        Set the value of the EmailSubject input for this Choreo. ((optional, string) The subject line of the email that PayPal sends when the transaction is completed. Character length and limitations: 255 single-byte alphanumeric characters.)
        """
        super(MakeIndividualPaymentInputSet, self)._set_input('EmailSubject', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The API Password provided by PayPal.)
        """
        super(MakeIndividualPaymentInputSet, self)._set_input('Password', value)
    def set_PaymentAmount(self, value):
        """
        Set the value of the PaymentAmount input for this Choreo. ((required, decimal) The amount to be paid.)
        """
        super(MakeIndividualPaymentInputSet, self)._set_input('PaymentAmount', value)
    def set_Signature(self, value):
        """
        Set the value of the Signature input for this Choreo. ((required, string) The API Signature provided by PayPal.)
        """
        super(MakeIndividualPaymentInputSet, self)._set_input('Signature', value)
    def set_UseSandbox(self, value):
        """
        Set the value of the UseSandbox input for this Choreo. ((conditional, boolean) Set to 1 to indicate that you're testing against the PayPal sandbox instead of production. Set to 0 (the default) when moving to production.)
        """
        super(MakeIndividualPaymentInputSet, self)._set_input('UseSandbox', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The API Username provided by PayPal.)
        """
        super(MakeIndividualPaymentInputSet, self)._set_input('Username', value)

class MakeIndividualPaymentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MakeIndividualPayment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The full response from PayPal formatted in name/value pairs.)
        """
        return self._output.get('Response', None)
    def get_Acknowledged(self):
        """
        Retrieve the value for the "Acknowledged" output from this Choreo execution. ((string) Indicates the status of the request. Should contain "Sucess" or "Failure".)
        """
        return self._output.get('Acknowledged', None)
    def get_CorrelationId(self):
        """
        Retrieve the value for the "CorrelationId" output from this Choreo execution. ((string) A unique id returned by PayPal for this payment.)
        """
        return self._output.get('CorrelationId', None)
    def get_ErrorMessage(self):
        """
        Retrieve the value for the "ErrorMessage" output from this Choreo execution. ((string) This will contain any error message returned by PayPal during this operation.)
        """
        return self._output.get('ErrorMessage', None)
    def get_Timestamp(self):
        """
        Retrieve the value for the "Timestamp" output from this Choreo execution. ((date) The timestamp associated with the payment request.)
        """
        return self._output.get('Timestamp', None)

class MakeIndividualPaymentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return MakeIndividualPaymentResultSet(response, path)
