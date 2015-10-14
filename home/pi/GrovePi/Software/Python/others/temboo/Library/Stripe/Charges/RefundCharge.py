# -*- coding: utf-8 -*-

###############################################################################
#
# RefundCharge
# Issues a refund of an existing credit card charge.
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

class RefundCharge(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RefundCharge Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RefundCharge, self).__init__(temboo_session, '/Library/Stripe/Charges/RefundCharge')


    def new_input_set(self):
        return RefundChargeInputSet()

    def _make_result_set(self, result, path):
        return RefundChargeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RefundChargeChoreographyExecution(session, exec_id, path)

class RefundChargeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RefundCharge
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(RefundChargeInputSet, self)._set_input('APIKey', value)
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((optional, integer) The amount to refund to the customer in cents. When left empty, the entire charge is refunded.)
        """
        super(RefundChargeInputSet, self)._set_input('Amount', value)
    def set_ChargeID(self, value):
        """
        Set the value of the ChargeID input for this Choreo. ((required, string) The unique identifier of the charge to be refunded)
        """
        super(RefundChargeInputSet, self)._set_input('ChargeID', value)

class RefundChargeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RefundCharge Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class RefundChargeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RefundChargeResultSet(response, path)
