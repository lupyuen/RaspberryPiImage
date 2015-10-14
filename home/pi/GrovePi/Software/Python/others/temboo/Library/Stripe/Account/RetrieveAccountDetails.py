# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveAccountDetails
# Retrieves the details of the account.
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

class RetrieveAccountDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveAccountDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RetrieveAccountDetails, self).__init__(temboo_session, '/Library/Stripe/Account/RetrieveAccountDetails')


    def new_input_set(self):
        return RetrieveAccountDetailsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveAccountDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveAccountDetailsChoreographyExecution(session, exec_id, path)

class RetrieveAccountDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveAccountDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        super(RetrieveAccountDetailsInputSet, self)._set_input('APIKey', value)

class RetrieveAccountDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveAccountDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)

class RetrieveAccountDetailsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RetrieveAccountDetailsResultSet(response, path)
