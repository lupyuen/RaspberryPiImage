# -*- coding: utf-8 -*-

###############################################################################
#
# RefundTransaction
# Issue a refund to a PayPal buyer by specifying a transaction ID.
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

class RefundTransaction(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RefundTransaction Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RefundTransaction, self).__init__(temboo_session, '/Library/PayPal/Merchant/RefundTransaction')


    def new_input_set(self):
        return RefundTransactionInputSet()

    def _make_result_set(self, result, path):
        return RefundTransactionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RefundTransactionChoreographyExecution(session, exec_id, path)

class RefundTransactionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RefundTransaction
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((optional, decimal) Refund amount. Amount is required if RefundType is set to Partial. If RefundType is set to Full, leave input blank.)
        """
        super(RefundTransactionInputSet, self)._set_input('Amount', value)
    def set_CurrencyCode(self, value):
        """
        Set the value of the CurrencyCode input for this Choreo. ((optional, string) A three-character currency code (i.e. USD). Required for partial refunds. Leave this field blank for full refunds. Defaults to USD.)
        """
        super(RefundTransactionInputSet, self)._set_input('CurrencyCode', value)
    def set_InvoiceID(self, value):
        """
        Set the value of the InvoiceID input for this Choreo. ((optional, string) Your own invoice or tracking number. Character length limitation is 127 alphanumeric characters.)
        """
        super(RefundTransactionInputSet, self)._set_input('InvoiceID', value)
    def set_Note(self, value):
        """
        Set the value of the Note input for this Choreo. ((optional, string) Custom note about the refund. Character length limitation is 255 alphanumeric characters.)
        """
        super(RefundTransactionInputSet, self)._set_input('Note', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The API Password provided by PayPal.)
        """
        super(RefundTransactionInputSet, self)._set_input('Password', value)
    def set_RefundType(self, value):
        """
        Set the value of the RefundType input for this Choreo. ((required, string) The refund type must be set to Full or Partial.  This flag effects what values some other input variables should have. Defaults to Full.)
        """
        super(RefundTransactionInputSet, self)._set_input('RefundType', value)
    def set_Signature(self, value):
        """
        Set the value of the Signature input for this Choreo. ((required, string) The API Signature provided by PayPal.)
        """
        super(RefundTransactionInputSet, self)._set_input('Signature', value)
    def set_TransactionID(self, value):
        """
        Set the value of the TransactionID input for this Choreo. ((required, string) The ID for the transaction you want to retrieve data for.)
        """
        super(RefundTransactionInputSet, self)._set_input('TransactionID', value)
    def set_UseSandbox(self, value):
        """
        Set the value of the UseSandbox input for this Choreo. ((conditional, boolean) Set to 1 to indicate that you're testing against the PayPal sandbox instead of production. Set to 0 (the default) when moving to production.)
        """
        super(RefundTransactionInputSet, self)._set_input('UseSandbox', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The API Username provided by PayPal.)
        """
        super(RefundTransactionInputSet, self)._set_input('Username', value)

class RefundTransactionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RefundTransaction Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) Response from PayPal formatted in name/value pairs.)
        """
        return self._output.get('Response', None)

class RefundTransactionChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RefundTransactionResultSet(response, path)
