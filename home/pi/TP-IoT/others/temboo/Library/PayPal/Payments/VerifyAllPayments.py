# -*- coding: utf-8 -*-

###############################################################################
#
# VerifyAllPayments
# Verifies that a payment has been successfully completed.
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

class VerifyAllPayments(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the VerifyAllPayments Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(VerifyAllPayments, self).__init__(temboo_session, '/Library/PayPal/Payments/VerifyAllPayments')


    def new_input_set(self):
        return VerifyAllPaymentsInputSet()

    def _make_result_set(self, result, path):
        return VerifyAllPaymentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VerifyAllPaymentsChoreographyExecution(session, exec_id, path)

class VerifyAllPaymentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the VerifyAllPayments
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved from PayPal. Required unless providing the ClientID and ClientSecret which can be used to generate a new access token.)
        """
        super(VerifyAllPaymentsInputSet, self)._set_input('AccessToken', value)
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((conditional, string) Your PayPal AppID (or the default AppID for the PayPal sandbox: APP-80W284485P519543T). This is used to authenticate PayPal's Adaptive Payments API.)
        """
        super(VerifyAllPaymentsInputSet, self)._set_input('AppID', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by PayPal. This is used to authenticate PayPal's REST API.)
        """
        super(VerifyAllPaymentsInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by PayPal. This is used to authenticate PayPal's REST API.)
        """
        super(VerifyAllPaymentsInputSet, self)._set_input('ClientSecret', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((conditional, string) The API Password provided by PayPal. This is used to authenticate PayPal's Adaptive Payments API.)
        """
        super(VerifyAllPaymentsInputSet, self)._set_input('Password', value)
    def set_ProofOfPayment(self, value):
        """
        Set the value of the ProofOfPayment input for this Choreo. ((required, json) The proof of payment received from the client SDK. This can be a proof of payment received from the Adaptive Payment API or the REST API.)
        """
        super(VerifyAllPaymentsInputSet, self)._set_input('ProofOfPayment', value)
    def set_Signature(self, value):
        """
        Set the value of the Signature input for this Choreo. ((conditional, string) The API Signature provided by PayPal. This is used to authenticate PayPal's Adaptive Payments API.)
        """
        super(VerifyAllPaymentsInputSet, self)._set_input('Signature', value)
    def set_UseSandbox(self, value):
        """
        Set the value of the UseSandbox input for this Choreo. ((conditional, boolean) Set to 1 to indicate that you're testing against the PayPal sandbox instead of production. Set to 0 (the default) when moving to production.)
        """
        super(VerifyAllPaymentsInputSet, self)._set_input('UseSandbox', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) The API Username provided by PayPal. This is used to authenticate PayPal's Adaptive Payments API.)
        """
        super(VerifyAllPaymentsInputSet, self)._set_input('Username', value)

class VerifyAllPaymentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the VerifyAllPayments Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PayPal. This includes the full response from retrieving payment details from either the AdaptivePayments API or the Rest API.)
        """
        return self._output.get('Response', None)
    def get_FailureDescription(self):
        """
        Retrieve the value for the "FailureDescription" output from this Choreo execution. ((json) When the payment details indicate that the payment status is not complete, this will contain a JSON dictionary of payment status descriptions.)
        """
        return self._output.get('FailureDescription', None)
    def get_VerificationStatus(self):
        """
        Retrieve the value for the "VerificationStatus" output from this Choreo execution. ((string) The status of the payment verification. This will set to either "verified" or "unverified" depending on the status of the payment details.)
        """
        return self._output.get('VerificationStatus', None)

class VerifyAllPaymentsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return VerifyAllPaymentsResultSet(response, path)
