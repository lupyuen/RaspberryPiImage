# -*- coding: utf-8 -*-

###############################################################################
#
# PaymentDetails
# Retrieves information about a specific payment.
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

class PaymentDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PaymentDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PaymentDetails, self).__init__(temboo_session, '/Library/PayPal/AdaptivePayments/PaymentDetails')


    def new_input_set(self):
        return PaymentDetailsInputSet()

    def _make_result_set(self, result, path):
        return PaymentDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PaymentDetailsChoreographyExecution(session, exec_id, path)

class PaymentDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PaymentDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) Your PayPal AppID (or the default AppID for the PayPal sandbox).)
        """
        super(PaymentDetailsInputSet, self)._set_input('AppID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The API Password provided by PayPal.)
        """
        super(PaymentDetailsInputSet, self)._set_input('Password', value)
    def set_PayKey(self, value):
        """
        Set the value of the PayKey input for this Choreo. ((conditional, string) The pay key that identifies the payment for which you want to retrieve details. This is the pay key returned in the response of the Pay method.)
        """
        super(PaymentDetailsInputSet, self)._set_input('PayKey', value)
    def set_Signature(self, value):
        """
        Set the value of the Signature input for this Choreo. ((required, string) The API Signature provided by PayPal.)
        """
        super(PaymentDetailsInputSet, self)._set_input('Signature', value)
    def set_TrackingID(self, value):
        """
        Set the value of the TrackingID input for this Choreo. ((optional, string) The tracking ID that was specified for this payment in the PayRequest message.)
        """
        super(PaymentDetailsInputSet, self)._set_input('TrackingID', value)
    def set_TransactionID(self, value):
        """
        Set the value of the TransactionID input for this Choreo. ((optional, string) The PayPal transaction ID associated with the payment. The Instant Payment Notification message associated with the payment contains the transaction ID.)
        """
        super(PaymentDetailsInputSet, self)._set_input('TransactionID', value)
    def set_UseSandbox(self, value):
        """
        Set the value of the UseSandbox input for this Choreo. ((conditional, boolean) Set to 1 to indicate that you're testing against the PayPal sandbox instead of production. Set to 0 (the default) when moving to production.)
        """
        super(PaymentDetailsInputSet, self)._set_input('UseSandbox', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The API Username provided by PayPal.)
        """
        super(PaymentDetailsInputSet, self)._set_input('Username', value)

class PaymentDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PaymentDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PayPal.)
        """
        return self._output.get('Response', None)
    def get_AccountID(self):
        """
        Retrieve the value for the "AccountID" output from this Choreo execution. ((string) The account id of the payment reciever.)
        """
        return self._output.get('AccountID', None)
    def get_Amount(self):
        """
        Retrieve the value for the "Amount" output from this Choreo execution. ((decimal) The payment amount.)
        """
        return self._output.get('Amount', None)
    def get_CurrencyCode(self):
        """
        Retrieve the value for the "CurrencyCode" output from this Choreo execution. ((string) The currency code for the payment.)
        """
        return self._output.get('CurrencyCode', None)
    def get_Email(self):
        """
        Retrieve the value for the "Email" output from this Choreo execution. ((string) The receiver email address.)
        """
        return self._output.get('Email', None)
    def get_Status(self):
        """
        Retrieve the value for the "Status" output from this Choreo execution. ((string) The status of the payment.)
        """
        return self._output.get('Status', None)
    def get_TransactionStatus(self):
        """
        Retrieve the value for the "TransactionStatus" output from this Choreo execution. ((string) The transaction status of the payment.)
        """
        return self._output.get('TransactionStatus', None)

class PaymentDetailsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PaymentDetailsResultSet(response, path)
