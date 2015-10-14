# -*- coding: utf-8 -*-

###############################################################################
#
# MassPayments
# Generates multiple payments from your PayPal Premier account or Business account to existing PayPal account holders.
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

class MassPayments(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MassPayments Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(MassPayments, self).__init__(temboo_session, '/Library/PayPal/Merchant/MassPayments')


    def new_input_set(self):
        return MassPaymentsInputSet()

    def _make_result_set(self, result, path):
        return MassPaymentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MassPaymentsChoreographyExecution(session, exec_id, path)

class MassPaymentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MassPayments
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_InputFile(self, value):
        """
        Set the value of the InputFile input for this Choreo. ((required, any) An input file containing the payments to process. This data can either be in CSV or XML format. The format should be indicated using the InputFormat input. See Choreo documentation for schema details.)
        """
        super(MassPaymentsInputSet, self)._set_input('InputFile', value)
    def set_EmailSubject(self, value):
        """
        Set the value of the EmailSubject input for this Choreo. ((optional, string) The subject line of the email that PayPal sends when the transaction is completed. This is the same for all recipients. Character length and limitations: 255 single-byte alphanumeric characters.)
        """
        super(MassPaymentsInputSet, self)._set_input('EmailSubject', value)
    def set_InputFormat(self, value):
        """
        Set the value of the InputFormat input for this Choreo. ((required, string) The type of input you are providing for this mass payment. Accepted values are "csv" or "xml". See Choreo documentation for expected schema details.)
        """
        super(MassPaymentsInputSet, self)._set_input('InputFormat', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The API Password provided by PayPal.)
        """
        super(MassPaymentsInputSet, self)._set_input('Password', value)
    def set_Signature(self, value):
        """
        Set the value of the Signature input for this Choreo. ((required, string) The API Signature provided by PayPal.)
        """
        super(MassPaymentsInputSet, self)._set_input('Signature', value)
    def set_UseSandbox(self, value):
        """
        Set the value of the UseSandbox input for this Choreo. ((conditional, boolean) Set to 1 to indicate that you're testing against the PayPal sandbox instead of production. Set to 0 (the default) when moving to production.)
        """
        super(MassPaymentsInputSet, self)._set_input('UseSandbox', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The API Username provided by PayPal.)
        """
        super(MassPaymentsInputSet, self)._set_input('Username', value)


class MassPaymentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MassPayments Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Result(self):
        """
        Retrieve the value for the "Result" output from this Choreo execution. (The MassPayment result from PayPal returned in the same format you've submitted.)
        """
        return self._output.get('Result', None)

class MassPaymentsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return MassPaymentsResultSet(response, path)
