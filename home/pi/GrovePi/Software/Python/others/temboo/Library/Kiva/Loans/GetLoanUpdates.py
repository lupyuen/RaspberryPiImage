# -*- coding: utf-8 -*-

###############################################################################
#
# GetLoanUpdates
# Returns all status updates for a loan, newest first.
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

class GetLoanUpdates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLoanUpdates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLoanUpdates, self).__init__(temboo_session, '/Library/Kiva/Loans/GetLoanUpdates')


    def new_input_set(self):
        return GetLoanUpdatesInputSet()

    def _make_result_set(self, result, path):
        return GetLoanUpdatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLoanUpdatesChoreographyExecution(session, exec_id, path)

class GetLoanUpdatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLoanUpdates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        super(GetLoanUpdatesInputSet, self)._set_input('AppID', value)
    def set_LoanID(self, value):
        """
        Set the value of the LoanID input for this Choreo. ((required, string) The ID of the loan for which to get details.)
        """
        super(GetLoanUpdatesInputSet, self)._set_input('LoanID', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Output returned can be XML or JSON. Defaults to JSON.)
        """
        super(GetLoanUpdatesInputSet, self)._set_input('ResponseType', value)

class GetLoanUpdatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLoanUpdates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Kiva.)
        """
        return self._output.get('Response', None)

class GetLoanUpdatesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLoanUpdatesResultSet(response, path)
